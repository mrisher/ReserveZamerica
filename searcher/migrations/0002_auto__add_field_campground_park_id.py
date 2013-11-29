# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Campground.park_id'
        db.add_column(u'searcher_campground', 'park_id',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=-1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Campground.park_id'
        db.delete_column(u'searcher_campground', 'park_id')


    models = {
        u'searcher.campground': {
            'Meta': {'object_name': 'Campground'},
            'campground_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'park_id': ('django.db.models.fields.SmallIntegerField', [], {})
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