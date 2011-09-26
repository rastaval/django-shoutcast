from django.http import HttpResponse, HttpResponseRedirect
from dj.models import DjShow, ShowArchive
from django.shortcuts import render_to_response
from django.template import RequestContext
from dj.forms import ShowForm
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.conf import settings
from utils.trans_api import ApiQuery
from time import gmtime, strftime
import random
import string
from django.contrib import messages
import redis


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
api = ApiQuery(settings.API_URL, settings.API_USER, settings.API_PASS)

def shows(request):
    shows = ShowArchive.objects.order_by('-date')

    return render_to_response('dj/show_list.html', {
        "shows": shows,
    }, context_instance=RequestContext(request))

def showpage(request, id):
    page = ShowArchive.objects.get(id=id)

    return render_to_response('dj/show.html', {
        "page": page,
    }, context_instance=RequestContext(request))


def startshow(request):
    pass

@login_required
def editshow(request):
    djshow = DjShow.objects.get(dj=request.user)
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            show = DjShow.objects.get(dj=request.user) 
            title = form.cleaned_data['show_name']
            description = form.cleaned_data['description']

            show.show_name = title
            show.description = description
            show.dj = request.user
            show.save()
            
            messages.add_message(request, messages.INFO, 'Show Updated~')

    else:
        form = ShowForm(initial={'show_name': djshow.show_name, 'description': djshow.description})

    return render_to_response('dj/editshow.html', {
        "djshow": djshow,
        "form": form,
    }, context_instance=RequestContext(request))

@login_required
def requestshow(request):
    status = api.request(op="getstatus", seq="420")
    source = status['data']['status']['activeresource']['source']

    if source == 'dj':
        track = 'dj'
    else:
        track = 'playlist'
    return render_to_response('dj/requestshow.html', {
       "track": track,
       }, context_instance=RequestContext(request))

@login_required
def addshow(request):
    show_info = DjShow.objects.get(dj=request.user)
    show_name = show_info.show_name

    if r.get('dj_ison'):
        messages.error(request, "A DJ is already on bro.")
        return HttpResponseRedirect('/')

    else:
        passcrap = ''.join(random.choice(string.ascii_uppercase) for x in range(5)) 
        api.request(op="modifydj", seq="420", name="dj", password=passcrap, priority=8)
        start_time = strftime("%H:%M", gmtime())
    
        r.set('dj_pass', passcrap)
        r.set('dj_timestart', start_time)
        r.set('dj_name', request.user.username)
        r.set('dj_showname', show_name)
        r.set('dj_ison', 'yes')

        r.expire('dj_pass', 3600)
        r.expire('dj_timestart', 3600)
        r.expire('dj_name', 3600)
        r.expire('dj_showname', 3600)
        r.expire('dj_ison', 3600)

        messages.success(request, 'You may now login: radio.cattes.us:8500 dj:%s' % r.get('dj_pass'))
        return HttpResponseRedirect('/')
