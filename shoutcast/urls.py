from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import ListView, DetailView
from music.models import Song, Artist, Genre, Album

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", "music.views.index", name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
    url(r"^profiles/", include("idios.urls")),
    url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
    url(r"^management/", include("management.urls")),
    url(r"^show/(?P<id>\d)/$", "dj.views.showpage", name="dj_show"),
    url(r"^shows/", "dj.views.shows", name="show_list"),
    url(r"^editshow/", "dj.views.editshow", name="show_edit"),
    url(r"^addshow/", "dj.views.addshow", name="add_show"),

    url(r"^artists/", ListView.as_view(
            queryset=Artist.objects.order_by('artist'),
            template_name='music/artist_list.html',
            paginate_by=15,
    )),
    url(r"^genres/", ListView.as_view(
            queryset=Genre.objects.order_by('genre'),
            template_name='music/genre_list.html',
            paginate_by=15,
    )),
    url(r"^albums/", ListView.as_view(
            queryset=Album.objects.order_by('album'),
            template_name='music/album_list.html',
            paginate_by=15,
    )),

    url(r"^album/(?P<pk>\d+)/$", "music.views.view_album", name="album_view"),
    url(r"^artist/(?P<pk>\d+)/$", "music.views.view_artist", name="artist_view"),
    url(r"^genre/(?P<pk>\d+)/$", "music.views.view_genre", name="genre_view"),

    url(r"^song/(?P<pk>\d+)/$", DetailView.as_view(
            model=Song,
            template_name="music/detail.html",
    )),

    url(r"^search/", include('haystack.urls')),
    url(r"^addsong/(?P<song>\d+)/$", "playlist.views.add_to_playlist", name="add_to_playlist"),
    url(r"^upload/", "music.views.upload_music", name="music_upload"),
    url(r"^stopdj/", "dj.views.leavestream", name="stop_show"),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
