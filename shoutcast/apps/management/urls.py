from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template



urlpatterns = patterns("",
    url(r"^$", "management.views.index", name="manage_index"),
    url(r"logs/", "management.views.logger", name="manage_logs"),
    url(r"queue/", "management.views.queue", name="manage_queue"),
    url(r"track/", "management.views.showinfo", name="manage_track"),
    url(r"status/", "management.views.status", name="manage_status"),
)