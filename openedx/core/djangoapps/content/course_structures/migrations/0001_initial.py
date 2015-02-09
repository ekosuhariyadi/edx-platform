# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CourseStructure'
        db.create_table('course_structures_coursestructure', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('course_id', self.gf('xmodule_django.models.CourseKeyField')(max_length=255, db_index=True)),
            ('version', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('structure_json', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('course_structures', ['CourseStructure'])

        # Adding unique constraint on 'CourseStructure', fields ['course_id', 'version']
        db.create_unique('course_structures_coursestructure', ['course_id', 'version'])


    def backwards(self, orm):
        # Removing unique constraint on 'CourseStructure', fields ['course_id', 'version']
        db.delete_unique('course_structures_coursestructure', ['course_id', 'version'])

        # Deleting model 'CourseStructure'
        db.delete_table('course_structures_coursestructure')


    models = {
        'course_structures.coursestructure': {
            'Meta': {'unique_together': "(('course_id', 'version'),)", 'object_name': 'CourseStructure'},
            'course_id': ('xmodule_django.models.CourseKeyField', [], {'max_length': '255', 'db_index': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'structure_json': ('django.db.models.fields.TextField', [], {}),
            'version': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['course_structures']