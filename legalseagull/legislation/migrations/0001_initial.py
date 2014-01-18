# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Title'
        db.create_table(u'legislation_title', (
            ('number', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'legislation', ['Title'])

        # Adding model 'Chapter'
        db.create_table(u'legislation_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['legislation.Title'])),
        ))
        db.send_create_signal(u'legislation', ['Chapter'])

        # Adding model 'Section'
        db.create_table(u'legislation_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('chapter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['legislation.Chapter'])),
        ))
        db.send_create_signal(u'legislation', ['Section'])


    def backwards(self, orm):
        # Deleting model 'Title'
        db.delete_table(u'legislation_title')

        # Deleting model 'Chapter'
        db.delete_table(u'legislation_chapter')

        # Deleting model 'Section'
        db.delete_table(u'legislation_section')


    models = {
        u'legislation.chapter': {
            'Meta': {'ordering': "['number']", 'object_name': 'Chapter'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['legislation.Title']"})
        },
        u'legislation.section': {
            'Meta': {'ordering': "['number']", 'object_name': 'Section'},
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['legislation.Chapter']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'legislation.title': {
            'Meta': {'ordering': "['number']", 'object_name': 'Title'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['legislation']