# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Volunteer'
        db.create_table(u'volition_volunteer', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(default=None, max_length=254, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(default=None, max_length=16, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(default=None, max_length=254, null=True, blank=True)),
            ('other', self.gf('django.db.models.fields.CharField')(default=None, max_length=120, null=True, blank=True)),
        ))
        db.send_create_signal(u'volition', ['Volunteer'])

        # Adding model 'Training'
        db.create_table(u'volition_training', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volunteer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['volition.Volunteer'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=2014)),
            ('location', self.gf('django.db.models.fields.CharField')(default=None, max_length=254, null=True, blank=True)),
            ('expiration_year', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
            ('remind', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'volition', ['Training'])

        # Adding model 'Experience'
        db.create_table(u'volition_experience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volunteer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['volition.Volunteer'])),
            ('event_year', self.gf('django.db.models.fields.IntegerField')(default=2014)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('work_hours', self.gf('django.db.models.fields.DecimalField')(default=4.0, null=True, max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'volition', ['Experience'])


    def backwards(self, orm):
        # Deleting model 'Volunteer'
        db.delete_table(u'volition_volunteer')

        # Deleting model 'Training'
        db.delete_table(u'volition_training')

        # Deleting model 'Experience'
        db.delete_table(u'volition_experience')


    models = {
        u'volition.experience': {
            'Meta': {'ordering': "['-event_year', 'event_name']", 'object_name': 'Experience'},
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'event_year': ('django.db.models.fields.IntegerField', [], {'default': '2014'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['volition.Volunteer']"}),
            'work_hours': ('django.db.models.fields.DecimalField', [], {'default': '4.0', 'null': 'True', 'max_digits': '6', 'decimal_places': '2'})
        },
        u'volition.training': {
            'Meta': {'ordering': "['name', '-year', '-expiration_year']", 'object_name': 'Training'},
            'expiration_year': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'remind': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['volition.Volunteer']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '2014'})
        },
        u'volition.volunteer': {
            'Meta': {'ordering': "['last_name', 'first_name']", 'object_name': 'Volunteer'},
            'address': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': 'None', 'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['volition']