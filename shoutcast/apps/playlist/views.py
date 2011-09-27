import urllib, urllib2
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.cache import cache
from django.contrib import messages
from music.models import Song
from dj.models import DjShow, CoolLinks, ShowArchive
from playlist.models import RecentTracks
from xml.etree import cElementTree as ElementTree
from utils.XmlToDict import XmlDictConfig
import redis
from utils.trans_api import ApiQuery
from apps.music.models import Album, Artist, Genre



r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

@login_required
def add_to_playlist(request, song):
    try:
        s = Song.objects.get(id=song)
    except:
        messages.error(request, "Song does not exist.")
        return HttpResponseRedirect

    if song in r.lrange('recent', 0, 8):
        messages.error(request, "Sorry but that song was just played recently!")
        return HttpResponseRedirect('/')
    else:
        r.lpush("playlist", song)
        messages.success(request, "Song added!")
        return HttpResponseRedirect('/')
