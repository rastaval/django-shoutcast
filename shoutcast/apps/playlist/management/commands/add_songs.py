from django.core.management import BaseCommand
from django.http import HttpResponse
import os
from music.models import Upload
from django.conf import settings
import fnmatch
from mutagen.mp3 import MP3
from apps.music.models import Song, Album, Artist, Genre
from apps.music.song_info import SongInfo
from django.contrib.auth.models import User
from django.core.files import File



class Command(BaseCommand):
    args = '<abs path to music folder>'
    help = 'adds songs located in music folder to database'

    def handle(self, *args, **options):
        path = args[0]
        for root, dirnames, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, '*.mp3'):
                song_file_path = root + '/' + filename
                
                upload = Upload()
                userthing = User.objects.get(pk=1)

                with open(song_file_path, 'rb') as song_file:
                    try:
                        obj = Upload.objects.get(song_file=File(song_file))
                    except Upload.DoesNotExist:
                        upload.song_file.save(filename, File(song_file), save=False)
                        upload.user = userthing
                        upload.save()
                        self.stdout.write("added %s \n" % filename)
                    except:
                        pass
