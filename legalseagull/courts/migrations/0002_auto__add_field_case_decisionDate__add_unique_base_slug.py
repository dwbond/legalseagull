# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Case.decisionDate'
        db.add_column(u'courts_case', 'decisionDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 18, 0, 0)),
                      keep_default=False)

        # Adding unique constraint on 'Base', fields ['slug']
        db.create_unique(u'courts_base', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Base', fields ['slug']
        db.delete_unique(u'courts_base', ['slug'])

        # Deleting field 'Case.decisionDate'
        db.delete_column(u'courts_case', 'decisionDate')


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
            'opinions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courts.Opinion']", 'symmetrical': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courts.Tags']", 'symmetrical': 'False'})
        },
        u'courts.justice': {
            'Meta': {'object_name': 'Justice', '_ormbases': [u'courts.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courts.Base']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'courts.opinion': {
            'Meta': {'object_name': 'Opinion', '_ormbases': [u'courts.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courts.Base']", 'unique': 'True', 'primary_key': 'True'}),
            'writtenBy': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courts.Justice']", 'symmetrical': 'False'})
        },
        u'courts.tags': {
            'Meta': {'object_name': 'Tags', '_ormbases': [u'courts.Base']},
            u'base_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['courts.Base']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['courts']