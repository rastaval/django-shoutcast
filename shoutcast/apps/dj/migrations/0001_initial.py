# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DjPerson'
        db.create_table('dj_djperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('dj', ['DjPerson'])

        # Adding model 'DjShow'
        db.create_table('dj_djshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dj', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('show_name', self.gf('django.db.models.fields.CharField')(max_length=420, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('dj', ['DjShow'])

        # Adding model 'ShowArchive'
        db.create_table('dj_showarchive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('djshow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dj.DjShow'])),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, null=True, blank=True)),
            ('show_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('dj', ['ShowArchive'])

        # Adding model 'CoolLinks'
        db.create_table('dj_coollinks', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=420)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=420)),
        ))
        db.send_create_signal('dj', ['CoolLinks'])


    def backwards(self, orm):
        
        # Deleting model 'DjPerson'
        db.delete_table('dj_djperson')

        # Deleting model 'DjShow'
        db.delete_table('dj_djshow')

        # Deleting model 'ShowArchive'
        db.delete_table('dj_showarchive')

        # Deleting model 'CoolLinks'
        db.delete_table('dj_coollinks')


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
        'dj.coollinks': {
            'Meta': {'object_name': 'CoolLinks'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '420'})
        },
        'dj.djperson': {
            'Meta': {'object_name': 'DjPerson'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '420'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'dj.djshow': {
            'Meta': {'object_name': 'DjShow'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dj': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_name': ('django.db.models.fields.CharField', [], {'max_length': '420', 'null': 'True', 'blank': 'True'})
        },
        'dj.showarchive': {
            'Meta': {'object_name': 'ShowArchive'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'djshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dj.DjShow']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dj']
