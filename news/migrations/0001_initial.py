# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Submission'
        db.create_table('news_submission', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=240)),
            ('url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('upvotes', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('news', ['Submission'])

        # Adding model 'Comment'
        db.create_table('news_comment', (
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submission', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='comments', null=True, to=orm['news.Submission'])),
        ))
        db.send_create_signal('news', ['Comment'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Submission'
        db.delete_table('news_submission')

        # Deleting model 'Comment'
        db.delete_table('news_comment')
    
    
    models = {
        'news.comment': {
            'Meta': {'object_name': 'Comment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'to': "orm['news.Submission']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'news.submission': {
            'Meta': {'object_name': 'Submission'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        }
    }
    
    complete_apps = ['news']
