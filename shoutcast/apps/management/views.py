from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from music.models import Song

from utils.trans_api import ApiQuery
from xml.etree import cElementTree as ElementTree
from utils.XmlToDict import XmlDictConfig
import json
import urllib2



api = ApiQuery(settings.API_URL, settings.API_USER, settings.API_PASS)

def index(request):
    test = api.request(op="test", foo="bar", seq="20")
    data = test['data']['param'][0]['value']

    return render_to_response('management/index.html', {
        "data": data,
    }, context_instance=RequestContext(request))

def logger(request):
    log = api.request(op="logdata", seq="420")
    logs = log['data']['logdata']['entry'][0]
    jlog = json.dumps(logs)
    if request.is_ajax():
        return HttpResponse(jlog)
    else:
        return HttpResponse(logs)

def status(request):
    api_url = settings.API_URL
    url = api_url.split(':7999')[0] + ":8000/stats?sid=1"
    #return HttpResponse(url)
    xml_url = urllib2.urlopen(url)
    xml = xml_url.read()
    root = ElementTree.XML(xml)
    xmldict = XmlDictConfig(root)


def queue(request):
    song = Song.objects.order_by('?')[0]
    if request.is_ajax():
        s = song.file_path
        return HttpResponse(s)
    else:
        s = song.file_path
        return HttpResponse(s)

def showinfo(request):
    status = api.request(op="getstatus", seq="320")
    source = status['data']['status']['activesource']['source']

    if source == 'dj':
        track = 'Live Show'
    else:
        track = status['data']['status']['activesource']['currenttrack']

    track_info = {'source': source, 'track': track}
    if request.is_ajax():
        jtrack = json.dumps(track_info)
        return HttpResponse(jtrack)
    else:
        return HttpResponse(source)

def history(request):
    pass
