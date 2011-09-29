import urllib, urllib2
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.cache import cache

from music.models import Song, Upload
from dj.models import DjShow, CoolLinks, ShowArchive
from playlist.models import RecentTracks
from xml.etree import cElementTree as ElementTree
from utils.XmlToDict import XmlDictConfig
import redis
from utils.trans_api import ApiQuery
from apps.music.models import Album, Artist, Genre
from music.forms import UploadForm
from django.views.decorators.csrf import csrf_exempt


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
api = ApiQuery(settings.API_URL, settings.API_USER, settings.API_PASS)

@login_required
def index(request):
    rlist = r.lrange("recent", 0, -1)[:3]
    rsongs = Song.objects.filter(pk__in=rlist)

    if r.exists("comingup"):
        try:
            r_coming = r.lrange("playlist", -1, -1)[0]
            coming = Song.objects.get(id=r_coming)
        except:
            coming = None
    else:
        coming = None

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
        "songs": rsongs,
        "track": track,
        "current_song": current_song,
        "dj": str(current_dj),
        "shows": shows,
        "links": links,
        "user": request.user,
        "djpass": djpass,
        "coming": coming,
    }, context_instance=RequestContext(request))

@login_required
def view_album(request, pk):
    album = Album.objects.get(pk=pk)
    songs = album.song_set.all()
    return render_to_response('music/album_detail.html', {
        "songs": songs,
        "album": album,
    }, context_instance=RequestContext(request))

@login_required
def view_artist(request, pk):
    artist = Artist.objects.get(pk=pk)
    songs = artist.song_set.all()
    return render_to_response('music/artist_detail.html', {
        "songs": songs,
        "artist": artist,
    }, context_instance=RequestContext(request))

@login_required
def view_genre(request, pk):
    genre = Genre.objects.get(pk=pk)
    songs = genre.song_set.all()
    return render_to_response('music/genre_detail.html', {
        "genre": genre,
        "songs": songs,
    }, context_instance=RequestContext(request))

@csrf_exempt
@login_required
def music_upload_post(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        songthing = request.FILES['song_file']
        if form.is_valid():
            try:
                dest = open(songthing.name, "wb")
                for block in songthing.chunks():
                    dest.write(block)
                dest.close()

                newform = form.save(commit=False)
                newform.user = request.user
                newform.save()
            except:
                pass

        response = HttpResponse()
        response.write("%s\r\n" % songthing.name)
        return response
    else:
        return redirect('/')

@login_required
def upload_music(request):

    form = UploadForm()

    return render_to_response('music/upload.html', {
        "user": request.user,
        "form": form,
    }, context_instance=RequestContext(request))


