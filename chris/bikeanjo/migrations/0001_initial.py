# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('bikeanjo_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('is_bikeanjo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cycling_since', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('commute_by_bike', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('other_groups', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('social_networks', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('service_routes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('service_accompaniment', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('service_teach', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('service_institute', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('know_tech', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('know_security', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('know_law', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('know_routes', self.gf('django.db.models.fields.SmallIntegerField')(default=0, blank=True)),
            ('agreement_bikeanjo', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('bikeanjo', ['Profile'])

        # Adding model 'Point'
        db.create_table('bikeanjo_point', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bikeanjo.Profile'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('bikeanjo', ['Point'])

        # Adding model 'Request'
        db.create_table('bikeanjo_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='requests_made', null=True, to=orm['bikeanjo.Profile'])),
            ('bikeanjo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requests', null=True, to=orm['bikeanjo.Profile'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('departure', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True)),
            ('departure_label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('arrival', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True)),
            ('arrival_label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('info', self.gf('django.db.models.fields.TextField')()),
            ('agreement', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('bikeanjo', ['Request'])

        # Adding model 'RegistrationKey'
        db.create_table('bikeanjo_registrationkey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('activated', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('bikeanjo', ['RegistrationKey'])

    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('bikeanjo_profile')

        # Deleting model 'Point'
        db.delete_table('bikeanjo_point')

        # Deleting model 'Request'
        db.delete_table('bikeanjo_request')

        # Deleting model 'RegistrationKey'
        db.delete_table('bikeanjo_registrationkey')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bikeanjo.point': {
            'Meta': {'object_name': 'Point'},
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bikeanjo.Profile']"})
        },
        'bikeanjo.profile': {
            'Meta': {'object_name': 'Profile'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'agreement_bikeanjo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'commute_by_bike': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'cycling_since': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_bikeanjo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'know_law': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'know_routes': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'know_security': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'know_tech': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'blank': 'True'}),
            'other_groups': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'service_accompaniment': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'service_institute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'service_routes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'service_teach': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_networks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'bikeanjo.registrationkey': {
            'Meta': {'object_name': 'RegistrationKey'},
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'bikeanjo.request': {
            'Meta': {'object_name': 'Request'},
            'agreement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'arrival': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'arrival_label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bikeanjo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requests'", 'null': 'True', 'to': "orm['bikeanjo.Profile']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'departure': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'departure_label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'requests_made'", 'null': 'True', 'to': "orm['bikeanjo.Profile']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bikeanjo']
