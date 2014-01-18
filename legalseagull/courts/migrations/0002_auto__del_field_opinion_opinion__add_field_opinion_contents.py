# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Opinion.opinion'
        db.delete_column(u'courts_opinion', 'opinion')

        # Adding field 'Opinion.contents'
        db.add_column(u'courts_opinion', 'contents',
                      self.gf('django.db.models.fields.TextField')(default='Change me, bitch!'),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Opinion.opinion'
        raise RuntimeError("Cannot reverse this migration. 'Opinion.opinion' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Opinion.opinion'
        db.add_column(u'courts_opinion', 'opinion',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)

        # Deleting field 'Opinion.contents'
        db.delete_column(u'courts_opinion', 'contents')


    models = {
        u'courts.base': {
            'Meta': {'object_name': 'Base'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'courts.case': {
            'Meta': {'object_name': 'Case', '_ormbases': [u'courts.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courts.Base']", 'unique': 'True', 'primary_key': 'True'}),
            'decisionDate': ('django.db.models.fields.DateField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courts.Tags']", 'symmetrical': 'False'})
        },
        u'courts.justice': {
            'Meta': {'object_name': 'Justice', '_ormbases': [u'courts.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courts.Base']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'courts.opinion': {
            'Meta': {'object_name': 'Opinion', '_ormbases': [u'courts.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courts.Base']", 'unique': 'True', 'primary_key': 'True'}),
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courts.Case']"}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'writtenBy': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'opinions'", 'symmetrical': 'False', 'to': u"orm['courts.Justice']"})
        },
        u'courts.tags': {
            'Meta': {'object_name': 'Tags', '_ormbases': [u'courts.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courts.Base']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['courts']