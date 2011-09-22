from django.http import HttpResponse
from dj.models import DjShow
from django.shortcuts import render_to_response
from django.template import RequestContext



def shows(request):
    shows = DjShow.objects.order_by('date')

    return render_to_response('dj/show_list.html', {
        "shows": shows,
    }, context_instance=RequestContext(request))

def showpage(request, id):
    page = DjShow.objects.get(id=id)

    return render_to_response('dj/show.html', {
        "page": page,
    }, context_instance=RequestContext(request))

