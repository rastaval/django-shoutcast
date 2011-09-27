# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PlayList'
        db.create_table('playlist_playlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=420)),
        ))
        db.send_create_signal('playlist', ['PlayList'])

        # Adding model 'PlayListGroup'
        db.create_table('playlist_playlistgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Song'])),
            ('playlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playlist.PlayList'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('playlist', ['PlayListGroup'])

        # Adding model 'RecentTracks'
        db.create_table('playlist_recenttracks', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Song'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('playlist', ['RecentTracks'])


    def backwards(self, orm):
        
        # Deleting model 'PlayList'
        db.delete_table('playlist_playlist')

        # Deleting model 'PlayListGroup'
        db.delete_table('playlist_playlistgroup')

        # Deleting model 'RecentTracks'
        db.delete_table('playlist_recenttracks')


    models = {
        'music.album': {
            'Meta': {'object_name': 'Album'},
            'album': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'album_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'music.artist': {
            'Meta': {'object_name': 'Artist'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'artist_bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'artist_image': ('django.db.models.fields.CharField', [], {'max_length': '420', 'null': 'True', 'blank': 'True'}),
            'artist_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'artist_url': ('django.db.models.fields.CharField', [], {'max_length': '420', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'music.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'genre_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'music.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Album']", 'null': 'True', 'blank': 'True'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Artist']", 'null': 'True', 'blank': 'True'}),
            'bitrate': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'file_path': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Genre']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'playlist.playlist': {
            'Meta': {'object_name': 'PlayList'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['music.Song']", 'through': "orm['playlist.PlayListGroup']", 'symmetrical': 'False'})
        },
        'playlist.playlistgroup': {
            'Meta': {'object_name': 'PlayListGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'playlist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playlist.PlayList']"}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Song']"})
        },
        'playlist.recenttracks': {
            'Meta': {'object_name': 'RecentTracks'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Song']"})
        }
    }

    complete_apps = ['playlist']
