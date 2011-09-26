import urllib, urllib2
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.cache import cache

from music.models import Song
from dj.models import DjShow, CoolLinks, ShowArchive
from playlist.models import RecentTracks
from xml.etree import cElementTree as ElementTree
from utils.XmlToDict import XmlDictConfig
import redis
from utils.trans_api import ApiQuery



r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
api = ApiQuery(settings.API_URL, settings.API_USER, settings.API_PASS)

@login_required
def index(request):
    rsongs = RecentTracks.objects.order_by('-date')[1:9]

    status = api.request(op="getstatus", seq="420")

    if r.get('dj_name') == request.user.username:
        source = 'isdj'
    else:
        source = status['data']['status']['activesource']['source']

    get_pass = api.request(op="listdjs", name="dj", seq="420")
    djpass = get_pass['data']['djlist']['dj']['password']

    current_dj = r.get('dj_name')

    if source == 'dj':
        track = 'dj'
    elif source == 'isdj':
        track = 'isdj'
    elif source == 'playlist':
        track = 'playlist'
    else:
        track = 'FUCK'

    if track == 'playlist':
        playing = status['data']['status']['activesource']['currenttrack']
        current_song = Song.objects.get(file_path=playing)
    elif track == 'dj':
        current_song = r.get('dj_showname')
    else:
        current_song = r.get('dj_showname')


    shows = ShowArchive.objects.order_by('-date')[:10]
    links = CoolLinks.objects.order_by('-id')[:10]

    return render_to_response('homepage.html', {
        "songs":rsongs,
        "track": track,
        "current_song": current_song,
        "dj": str(current_dj),
        "shows": shows,
        "links": links,
        "user": request.user,
        "djpass": djpass,
    }, context_instance=RequestContext(request))

