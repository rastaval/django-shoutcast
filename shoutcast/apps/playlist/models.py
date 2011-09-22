from django.db import models
from music.models import Song


class PlayList(models.Model):
    name = models.CharField(max_length=420)
    songs = models.ManyToManyField(Song, through="PlayListGroup")

    def __unicode__(self):
        return u'%s' % self.name


class PlayListGroup(models.Model):
    song = models.ForeignKey(Song)
    playlist = models.ForeignKey(PlayList)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s - %s - %s' % (self.order, self.song, self.playlist)


class RecentTracks(models.Model):
    song = models.ForeignKey(Song)
    date = models.DateTimeField(auto_now=True, auto_now_add=True, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.song
