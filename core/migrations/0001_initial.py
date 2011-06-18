# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Cell'
        db.create_table('core_cell', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lock_dt', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Cell'])

        # Adding model 'Lock'
        db.create_table('core_lock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lock_dt', self.gf('django.db.models.fields.DateTimeField')()),
            ('cell', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Cell'])),
        ))
        db.send_create_signal('core', ['Lock'])


    def backwards(self, orm):
        
        # Deleting model 'Cell'
        db.delete_table('core_cell')

        # Deleting model 'Lock'
        db.delete_table('core_lock')


    models = {
        'core.cell': {
            'Meta': {'object_name': 'Cell'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lock_dt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'core.lock': {
            'Meta': {'object_name': 'Lock'},
            'cell': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Cell']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lock_dt': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['core']
