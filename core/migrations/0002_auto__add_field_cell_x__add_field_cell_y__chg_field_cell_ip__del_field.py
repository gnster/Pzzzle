# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Cell.x'
        db.add_column('core_cell', 'x', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'Cell.y'
        db.add_column('core_cell', 'y', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Changing field 'Cell.ip'
        db.alter_column('core_cell', 'ip', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Deleting field 'Lock.cell'
        db.delete_column('core_lock', 'cell_id')

        # Adding field 'Lock.x'
        db.add_column('core_lock', 'x', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'Lock.y'
        db.add_column('core_lock', 'y', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Cell.x'
        db.delete_column('core_cell', 'x')

        # Deleting field 'Cell.y'
        db.delete_column('core_cell', 'y')

        # Changing field 'Cell.ip'
        db.alter_column('core_cell', 'ip', self.gf('django.db.models.fields.CharField')(default=1, max_length=20))

        # Adding field 'Lock.cell'
        db.add_column('core_lock', 'cell', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Cell']), keep_default=False)

        # Deleting field 'Lock.x'
        db.delete_column('core_lock', 'x')

        # Deleting field 'Lock.y'
        db.delete_column('core_lock', 'y')


    models = {
        'core.cell': {
            'Meta': {'object_name': 'Cell'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lock_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.lock': {
            'Meta': {'object_name': 'Lock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lock_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'y': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']
