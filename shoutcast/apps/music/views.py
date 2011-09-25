import urllib, urllib2
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from music.models import Song
from dj.models import DjShow, CoolLinks, ShowArchive
from playlist.models import RecentTracks
from xml.etree import cElementTree as ElementTree
from utils.XmlToDict import XmlDictConfig

from utils.trans_api import ApiQuery


api = ApiQuery(settings.API_URL, settings.API_USER, settings.API_PASS)

def index(request):
    rsongs = RecentTracks.objects.order_by('-date')[1:9]

    status = api.request(op="getstatus", seq="420")
    source = status['data']['status']['activesource']['source']

    if source == 'dj':
        track = 'dj'
    else:
        track = 'playlist'

    if track == 'playlist':
        playing = status['data']['status']['activesource']['currenttrack']
        current_song = Song.objects.get(file_path=playing)

    elif track == 'dj':
        api_url = settings.API_URL
        url = api_url.split(':7999')[0] + ":9021/stats?sid=1"
        xml_url = urllib2.urlopen(url)
        xml = xml_url.read()
        root = ElementTree.XML(xml)
        xmldict = XmlDictConfig(root)
        current_song = xmldict['SERVERTITLE']

    else:
        current_song = 'dicks'


    shows = ShowArchive.objects.order_by('-date')[:10]
    links = CoolLinks.objects.order_by('-id')[:10]

    return render_to_response('homepage.html', {
        "songs":rsongs,
        "track": track,
        "current_song": current_song,
        "shows": shows,
        "links": links,
    }, context_instance=RequestContext(request))

