from django.http import HttpResponse
import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify
from django.conf import settings

from mutagen.mp3 import MP3
from song_info import SongInfo
from pyechonest import config
from pyechonest import artist as echoartist


api_key = settings.ECHOES_NEST_API_KEY
config.ECHO_NEST_API_KEY = api_key
fs = FileSystemStorage(location=settings.MUSIC_STORAGE_PATH, base_url=settings.MUSIC_URL)

class Song(models.Model):
    file_path = models.CharField(max_length=420)
    file_name = models.CharField(max_length=420)
    length = models.PositiveIntegerField()
    title = models.CharField(max_length=420)
    title_slug = models.SlugField()
    bitrate = models.PositiveIntegerField()
    artist = models.ForeignKey("Artist", blank=True, null=True)
    album = models.ForeignKey("Album", blank=True, null=True)
    genre = models.ForeignKey("Genre", blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.title

    def save(self, *args, **kwargs):
        self.title_slug = slugify(self.title)
        super(Song, self).save(*args, **kwargs)


class Upload(models.Model):
    song_file = models.FileField(storage=fs, upload_to="uploads/", max_length=100)
    user = models.ForeignKey(User)
    def __unicode__(self):
        return u'%s' % self.song_file

class Genre(models.Model):
    genre = models.CharField(max_length=420)
    genre_slug = models.SlugField()

    def __unicode__(self):
        return u'%s' % self.genre        
    
    def save(self, *args, **kwargs):    
        self.genre_slug = slugify(self.genre)                                                                  
        super(Genre, self).save(*args, **kwargs) 
    

class Artist(models.Model):
    artist = models.CharField(max_length=420)
    artist_slug = models.SlugField()
    artist_bio = models.TextField(blank=True, null=True)
    artist_url = models.CharField(max_length=420, blank=True, null=True)
    artist_image = models.CharField(max_length=420, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.artist

    def save(self, *args, **kwargs):    
        self.artist_slug = slugify(self.artist)
        artist_results = echoartist.search(name=self.artist)[0]
        bio = artist_results.biographies[0]
        image = artist_results.images[0]
        self.artist_image = image['url']
        self.artist_bio = bio['text']
        self.artist_url = bio['url']
        super(Artist, self).save(*args, **kwargs) 


class Album(models.Model):
    album = models.CharField(max_length=420)
    album_slug = models.SlugField()

    def __unicode__(self):
        return u'%s' % self.album
    
    def save(self, *args, **kwargs):    
        self.album_slug = slugify(self.album)
        super(Album, self).save(*args, **kwargs) 

#signals
def upload_to_song(sender, instance, created, **kwargs):
    """

    """
    if created:
        song_path = instance.song_file.path

        #song = Song()

        try:
            info = SongInfo(song_path)
        except:
            return HttpResponse('<h1>sorry for your shit music but i coldnt find any meta info about it.')
        
        file_info = MP3(song_path)
        meta = info.meta

        #oh god
        #TODO: rewrite this abortion
        try:
            song_length = meta['duration']
        except:
            song_length = 420
        try:
            song_artist = meta['artist']
        except:
            song_artist = "Unknown"
        try:
            song_title = meta['title']
        except:
            song_title = "Unknown"
        try:
            song_genre = meta['genre']
        except:
            song_genre = "Unknown"
        try:
            song_bitrate = meta['bitrate']
        except:
            song_bitrate = 320
        try:
            song_album = file_info["TALB"]
        except:
            song_album = "Unknown"

        genre, gcreated = Genre.objects.get_or_create(genre=song_genre)
        artist, acreated = Artist.objects.get_or_create(artist=song_artist)
        album, alcreated = Album.objects.get_or_create(album=song_album)
        
        crap = {
            "file_path": song_path,
            "length": song_length,
            "title": song_title,
            "bitrate": song_bitrate,
            "artist": artist,
            "genre": genre,
            "album": album,
            "file_name": os.path.basename(instance.song_file.name)
        }

        #song.file_path = song_path
        #song.length = song_length
        #song.title = song_title
        #song.bitrate = song_bitrate
        #song.artist = artist
        #song.album = album
        #song.genre = genre
        #song.file_name = os.path.basename(instance.song_file.name)
        #
        #song.save()

        song, created = Song.objects.get_or_create(**crap)

post_save.connect(upload_to_song, sender=Upload)
