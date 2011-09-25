from celery.decorators import task
from django.core.cache import cache
import datetime
from time import gmtime, strftime, strptime
import time
from utils.trans_api import ApiQuery
from django.conf import settings


api = ApiQuery(settings.API_URL, settings.API_USER, settings.API_PASS)

@task()
def check_dj():
    dj_timestart = cache.get('dj_timestart')
    timeformat = "%H:%M"
    djtime = time.strptime(dj_timestart, timeformat)

    if datetime.now() - djtime >= 3600:
        api.request(op="kickdj", seq=520) 
        cache.delete('dj_pass')
        cache.delete('dj_timestart')
        cache.delete('dj_name')
        cache.delete('dj_showname')

        return "dj kicked"
    else:
        return "no dj on"
