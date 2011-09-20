from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify
from django.conf import settings

from utils.song_info import SongInfo
from mutagen.mp3 import MP3


fs = FileSystemStorage(location=settings.MUSIC_STORAGE_PATH, base_url=settings.MUSIC_URL)

class Song(models.Model):
    file_path = models.CharField(max_length=420)
    length = models.PositiveIntegerField()
    title = models.CharField(max_length=420)
    title_slug = models.SlugField()
    bitrate = models.PositiveIntegerField()
    url = models.CharField(max_length=420)
    artist = models.ForeignKey("Artist", blank=True, null=True)
    album = models.ForeignKey("Album", blank=True, null=True)
    genre = models.ForeignKey("Genre", blank=True, null=True)
    user = models.ForeignKey(User)

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

    def __unicode__(self):
        return u'%s' % self.artist

    def save(self, *args, **kwargs):    
        self.artist_slug = slugify(self.artist)
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
    if created:
        song_path = instance.song_file.path

        song = Song()

        info = SongInfo(song_path)
        file_info = MP3(song_path)
        meta = info.meta
        
        song_length = meta['duration']
        song_artist = meta['artist']
        song_title = meta['title']
        song_genre = meta['genre']
        song_bitrate = meta['bitrate']
        song_album = file_info['TALB']

        genre, gcreated = Genre.objects.get_or_create(genre=song_genre)
        artist, acreated = Artist.objects.get_or_create(artist=song_artist)
        album, alcreated = Album.objects.get_or_create(album=song_album)

        song.file_path = song_path
        song.length = song_length
        song.title = song_title
        song.bitrate = song_bitrate
        song.url = instance.song_file.url
        song.artist = artist
        song.album = album
        song.genre = genre
        song.user = instance.user

        song.save()

post_save.connect(upload_to_song, sender=Upload)
