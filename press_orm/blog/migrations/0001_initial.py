# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table(u'blog_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Categoria'])

        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('texto', self.gf('django.db.models.fields.TextField')(max_length=1024)),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding M2M table for field categorias on 'Post'
        m2m_table_name = db.shorten_name(u'blog_post_categorias')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False)),
            ('categoria', models.ForeignKey(orm[u'blog.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'categoria_id'])

        # Adding model 'Comentarios'
        db.create_table(u'blog_comentarios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comentario', self.gf('django.db.models.fields.TextField')(max_length=1024)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comentarios', to=orm['blog.Post'])),
        ))
        db.send_create_signal(u'blog', ['Comentarios'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table(u'blog_categoria')

        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Removing M2M table for field categorias on 'Post'
        db.delete_table(db.shorten_name(u'blog_post_categorias'))

        # Deleting model 'Comentarios'
        db.delete_table(u'blog_comentarios')


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
            'texto': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']