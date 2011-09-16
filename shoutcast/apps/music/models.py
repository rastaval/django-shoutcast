from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import mutagen
from django.core.files.storage import FileSystemStorage
from utils.song_info import SongInfo
import slumber



ECHOES_NEST_API_KEY = "6ELTPYPVXF11BNXV0"
MUSIC_STORAGE_PATH = "/home/alan/Music/"
MUSIC_URL = "http://music.jonny290.com/"
fs = FileSystemStorage(location=MUSIC_STORAGE_PATH, base_url=MUSIC_URL)

class Song(models.Model):
    file_path = models.CharField(max_length=420, blank=True)
    length = models.PositiveIntegerField()
    title = models.CharField(max_length=420)
    bitrate = models.PositiveIntegerField()
    url = models.CharField(max_length=420)
    artist = models.ForeignKey("Artist", blank=True, null=True)
    album = models.ForeignKey("Album", blank=True, null=True)
    genre = models.ForeignKey("Genre", blank=True, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.title


class Upload(models.Model):
    song_file = models.FileField(storage=fs, upload_to="uploads/", max_length=100)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % self.song_file


class Genre(models.Model):
    genre = models.CharField(max_length=420)

    def __unicode__(self):
        return u'%s' % self.genre        
    

class Artist(models.Model):
    artist = models.CharField(max_length=420)

    def __unicode__(self):
        return u'%s' % self.artist


class Album(models.Model):
    album = models.CharField(max_length=420)

    def __unicode__(self):
        return u'%s' % self.album
    

#signals
def upload_to_song(sender, instance, created, **kwargs):
    if created:
        song_path = MUSIC_STORAGE_PATH + instance.song_file.path

        song = Song()

        info = SongInfo(song_path)
        file_info = mutagen.File(song_path, easy=True)
        meta = info.meta
        
        song_length = meta['length']
        song_artist = meta['artist']
        song_title = meta['title']
        song_genre = meta['genre']
        song_bitrate = meta['bitrate']
        song_date = file_info['date']
        song_album = file_info['album']

        genre = Genre.objects.get_or_create(genre=song_genre)
        artist = Artist.objects.get_or_create(artist=song_artist)
        album = Album.objects.get_or_create(album=song_album)

        song.file_path = song_path
        song.length = song_length
        song.title = song_title
        song.bitrate = song_bitrate
        song.url = instance.song_file.url
        song.date = song_date
        song.artist = artist
        song.album = album
        song.genres = genre
        user = instance.user

        song.save()

post_save.connect(upload_to_song, sender=Upload)
