# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Song'
        db.create_table('music_song', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_path', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('file_name', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('length', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('bitrate', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Artist'], null=True, blank=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Album'], null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Genre'], null=True, blank=True)),
        ))
        db.send_create_signal('music', ['Song'])

        # Adding model 'Upload'
        db.create_table('music_upload', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('music', ['Upload'])

        # Adding model 'Genre'
        db.create_table('music_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('genre_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('music', ['Genre'])

        # Adding model 'Artist'
        db.create_table('music_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('artist_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('artist_bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('artist_url', self.gf('django.db.models.fields.CharField')(max_length=420, null=True, blank=True)),
            ('artist_image', self.gf('django.db.models.fields.CharField')(max_length=420, null=True, blank=True)),
        ))
        db.send_create_signal('music', ['Artist'])

        # Adding model 'Album'
        db.create_table('music_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('album_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('music', ['Album'])


    def backwards(self, orm):
        
        # Deleting model 'Song'
        db.delete_table('music_song')

        # Deleting model 'Upload'
        db.delete_table('music_upload')

        # Deleting model 'Genre'
        db.delete_table('music_genre')

        # Deleting model 'Artist'
        db.delete_table('music_artist')

        # Deleting model 'Album'
        db.delete_table('music_album')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        'music.upload': {
            'Meta': {'object_name': 'Upload'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['music']
