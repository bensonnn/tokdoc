# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'core_patient')

        # Deleting model 'Doctor'
        db.delete_table(u'core_doctor')

        # Adding model 'DoctorProfile'
        db.create_table(u'core_doctorprofile', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.UserProfile'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['DoctorProfile'])

        # Adding model 'PatientProfile'
        db.create_table(u'core_patientprofile', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.UserProfile'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['PatientProfile'])

        # Adding model 'DoctorOnlineCall'
        db.create_table(u'core_doctoronlinecall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='doctor', to=orm['auth.User'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='patient', to=orm['auth.User'])),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['DoctorOnlineCall'])


    def backwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'core_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Patient'])

        # Adding model 'Doctor'
        db.create_table(u'core_doctor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Doctor'])

        # Deleting model 'DoctorProfile'
        db.delete_table(u'core_doctorprofile')

        # Deleting model 'PatientProfile'
        db.delete_table(u'core_patientprofile')

        # Deleting model 'DoctorOnlineCall'
        db.delete_table(u'core_doctoronlinecall')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.doctoronlinecall': {
            'Meta': {'object_name': 'DoctorOnlineCall'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'doctor'", 'to': u"orm['auth.User']"}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient'", 'to': u"orm['auth.User']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'core.doctorprofile': {
            'Meta': {'object_name': 'DoctorProfile', '_ormbases': [u'core.UserProfile']},
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.patientprofile': {
            'Meta': {'object_name': 'PatientProfile', '_ormbases': [u'core.UserProfile']},
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.userconnection': {
            'Meta': {'unique_together': "(('user_a', 'user_b'),)", 'object_name': 'UserConnection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_sent': ('django.db.models.fields.BooleanField', [], {}),
            'user_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_a'", 'to': u"orm['auth.User']"}),
            'user_a_requested_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_b'", 'to': u"orm['auth.User']"}),
            'user_b_accepted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'default': "'img/default_profile.png'", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.waitingroom': {
            'Meta': {'object_name': 'WaitingRoom'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['core']