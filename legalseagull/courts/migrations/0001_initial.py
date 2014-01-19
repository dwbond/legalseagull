# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Base'
        db.create_table(u'courts_base', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'courts', ['Base'])

        # Adding model 'Tags'
        db.create_table(u'courts_tags', (
            (u'base_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['courts.Base'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'courts', ['Tags'])

        # Adding model 'Justice'
        db.create_table(u'courts_justice', (
            (u'base_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['courts.Base'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'courts', ['Justice'])

        # Adding model 'Opinion'
        db.create_table(u'courts_opinion', (
            (u'base_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['courts.Base'], unique=True, primary_key=True)),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courts.Case'])),
        ))
        db.send_create_signal(u'courts', ['Opinion'])

        # Adding M2M table for field writtenBy on 'Opinion'
        m2m_table_name = db.shorten_name(u'courts_opinion_writtenBy')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('opinion', models.ForeignKey(orm[u'courts.opinion'], null=False)),
            ('justice', models.ForeignKey(orm[u'courts.justice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['opinion_id', 'justice_id'])

        # Adding model 'Case'
        db.create_table(u'courts_case', (
            (u'base_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['courts.Base'], unique=True, primary_key=True)),
            ('decisionDate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'courts', ['Case'])

        # Adding M2M table for field tags on 'Case'
        m2m_table_name = db.shorten_name(u'courts_case_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('case', models.ForeignKey(orm[u'courts.case'], null=False)),
            ('tags', models.ForeignKey(orm[u'courts.tags'], null=False))
        ))
        db.create_unique(m2m_table_name, ['case_id', 'tags_id'])


    def backwards(self, orm):
        # Deleting model 'Base'
        db.delete_table(u'courts_base')

        # Deleting model 'Tags'
        db.delete_table(u'courts_tags')

        # Deleting model 'Justice'
        db.delete_table(u'courts_justice')

        # Deleting model 'Opinion'
        db.delete_table(u'courts_opinion')

        # Removing M2M table for field writtenBy on 'Opinion'
        db.delete_table(db.shorten_name(u'courts_opinion_writtenBy'))

        # Deleting model 'Case'
        db.delete_table(u'courts_case')

        # Removing M2M table for field tags on 'Case'
        db.delete_table(db.shorten_name(u'courts_case_tags'))


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