from django.contrib import admin
from music.models import Song, Upload, Genre, Artist, Album


admin.site.register(Song)
admin.site.register(Upload)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
