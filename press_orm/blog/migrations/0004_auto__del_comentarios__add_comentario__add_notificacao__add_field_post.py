# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Comentarios'
        db.delete_table(u'blog_comentarios')

        # Adding model 'Comentario'
        db.create_table(u'blog_comentario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comentario', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comentarios', to=orm['blog.Post'])),
        ))
        db.send_create_signal(u'blog', ['Comentario'])

        # Adding model 'Notificacao'
        db.create_table(u'blog_notificacao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notifications', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'blog', ['Notificacao'])

        # Adding field 'Post.autor'
        db.add_column(u'blog_post', 'autor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Comentarios'
        db.create_table(u'blog_comentarios', (
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comentarios', to=orm['blog.Post'])),
            ('comentario', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'blog', ['Comentarios'])

        # Deleting model 'Comentario'
        db.delete_table(u'blog_comentario')

        # Deleting model 'Notificacao'
        db.delete_table(u'blog_notificacao')

        # Deleting field 'Post.autor'
        db.delete_column(u'blog_post', 'autor_id')


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
        u'blog.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blog.comentario': {
            'Meta': {'object_name': 'Comentario'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comentario': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comentarios'", 'to': u"orm['blog.Post']"})
        },
        u'blog.notificacao': {
            'Meta': {'object_name': 'Notificacao'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notifications'", 'to': u"orm['auth.User']"})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Categoria']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']