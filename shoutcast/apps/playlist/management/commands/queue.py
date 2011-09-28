from django.core.management.base import BaseCommand, CommandError
import os
from playlist.models import PlayList
from music.models import Song
from playlist.models import RecentTracks
from pyechonest import config
from pyechonest import artist
from django.conf import settings
import redis


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

class Command(BaseCommand):
    args = '<number of songs ahead>'
    help = "returns x amount of songs ahead in the playlist"

    def handle(self, *args, **options):
        if r.lindex("playlist", 0):
            #lpush songs into playlist
            r_song = r.rpop("playlist")
            song = Song.objects.get(id=r_song)
            r.rpush("recent", song.id)
            try:
                coming = r.lrange("playlist", 0, 0)[0]
            except:
                coming = None
            r.set("comingup", coming)
            self.stdout.write(song.file_path)

        else:
            song = Song.objects.order_by('?')[0]
            if song.id in r.lrange("recent", 0, 5):
                song = Song.objects.order_by('?')[0]
            r_artists = []
            for a in r.lrange("recent", 0, 5):
                s = Song.objects.get(id=a)
                r_artists.append(s.artist.artist)
            if song.artist.artist in r_artists:
                song = Song.objects.order_by('?')[0]
            r.lpush("recent", song.id)
            self.stdout.write(song.file_path)
