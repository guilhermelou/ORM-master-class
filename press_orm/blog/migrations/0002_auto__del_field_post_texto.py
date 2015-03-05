# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.texto'
        db.delete_column(u'blog_post', 'texto')


    def backwards(self, orm):
        # Adding field 'Post.texto'
        db.add_column(u'blog_post', 'texto',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=1024),
                      keep_default=False)


    models = {
        u'blog.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blog.comentarios': {
            'Meta': {'object_name': 'Comentarios'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comentario': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comentarios'", 'to': u"orm['blog.Post']"})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'categorias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Categoria']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']