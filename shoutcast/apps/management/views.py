from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from utils.trans_api import ApiQuery
import json


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

def tracks(request):
    status = api.request(op="getstatus", seq="320")


        