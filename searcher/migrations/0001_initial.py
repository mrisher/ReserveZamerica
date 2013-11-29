# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DayOfWeek'
        db.create_table(u'searcher_dayofweek', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day_name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'searcher', ['DayOfWeek'])

        # Adding model 'Campground'
        db.create_table(u'searcher_campground', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campground_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'searcher', ['Campground'])

        # Adding model 'CampgroundQuery'
        db.create_table(u'searcher_campgroundquery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campground', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['searcher.Campground'])),
            ('stay_length', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('last_query', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'searcher', ['CampgroundQuery'])

        # Adding M2M table for field eligible_days on 'CampgroundQuery'
        m2m_table_name = db.shorten_name(u'searcher_campgroundquery_eligible_days')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('campgroundquery', models.ForeignKey(orm[u'searcher.campgroundquery'], null=False)),
            ('dayofweek', models.ForeignKey(orm[u'searcher.dayofweek'], null=False))
        ))
        db.create_unique(m2m_table_name, ['campgroundquery_id', 'dayofweek_id'])

        # Adding model 'Result'
        db.create_table(u'searcher_result', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'searcher', ['Result'])


    def backwards(self, orm):
        # Deleting model 'DayOfWeek'
        db.delete_table(u'searcher_dayofweek')

        # Deleting model 'Campground'
        db.delete_table(u'searcher_campground')

        # Deleting model 'CampgroundQuery'
        db.delete_table(u'searcher_campgroundquery')

        # Removing M2M table for field eligible_days on 'CampgroundQuery'
        db.delete_table(db.shorten_name(u'searcher_campgroundquery_eligible_days'))

        # Deleting model 'Result'
        db.delete_table(u'searcher_result')


    models = {
        u'searcher.campground': {
            'Meta': {'object_name': 'Campground'},
            'campground_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'searcher.campgroundquery': {
            'Meta': {'object_name': 'CampgroundQuery'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'campground': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['searcher.Campground']"}),
            'eligible_days': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['searcher.DayOfWeek']", 'symmetrical': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_query': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'stay_length': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'searcher.dayofweek': {
            'Meta': {'object_name': 'DayOfWeek'},
            'day_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'searcher.result': {
            'Meta': {'object_name': 'Result'},
            'data': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['searcher']