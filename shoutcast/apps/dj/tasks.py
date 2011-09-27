from celery.decorators import task
from django.core.cache import cache
import datetime
from time import gmtime, strftime, strptime
import time
from utils.trans_api import ApiQuery
from django.conf import settings
import redis
import random
import string
from celery.task.schedules import crontab
from celery.decorators import periodic_task


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
api = ApiQuery(settings.API_URL, settings.API_USER, settings.API_PASS)

@periodic_task(run_every=crontab())
def check_dj():
    dj_check = r.get('dj_ison')
    if dj_check:
        pass
    else:
        randompass = ''.join(random.choice(string.ascii_uppercase) for x in range(10))
        api.request(op="kickdj", seq="520")
        api.request(op="modifydj", seq="620", name="dj", password=randompass, priority=8)
        api.request(op="unkickdj", seq="120", name="dj")
        r.delete('dj_pass', 'dj_timestart', 'dj_name', 'dj_showname', 'dj_ison')



