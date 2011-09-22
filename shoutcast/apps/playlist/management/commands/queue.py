from django.core.management.base import BaseCommand, CommandError
import os
from playlist.models import PlayList
from music.models import Song
from playlist.models import RecentTracks
from pyechonest import config
from pyechonest import artist
from django.conf import settings

config.ECHO_NEST_API_KEY = settings.ECHOES_NEST_API_KEY

class Command(BaseCommand):
    args = '<number of songs ahead>'
    help = "returns x amount of songs ahead in the playlist"

    def handle(self, *args, **options):
        song = Song.objects.order_by('?')[0]
        plist = RecentTracks()
        plist.song = song
        plist.save()
        self.stdout.write(song.file_path)