# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
# Create your models here.
class Notificacao(models.Model):
    title = models.CharField(u'Título', max_length=200)
    content = models.TextField(u'Conteúdo')
    user = models.ForeignKey(User, related_name='notifications')
    
    class Meta:
        verbose_name = (u'Notificação')
        verbose_name_plural = (u'Notificações')

    def __unicode__(self):
        return self.title

class Categoria(models.Model):

    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome


class Post(models.Model):

    autor = models.ForeignKey(User)
    titulo = models.CharField(max_length=200)
    texto = models.TextField(max_length=1024)
    categorias = models.ManyToManyField(Categoria)

    def __unicode__(self):
        return self.titulo


class Comentario(models.Model):

    autor = models.CharField(max_length=100)
    comentario = models.TextField(max_length=1024)
    post = models.ForeignKey(Post, related_name='comentarios')

    def __unicode__(self):
        return self.autor

@receiver(post_save, sender=Comentario)
def notify_comentario(sender, **kwargs):
    comentario = kwargs.get('instance')
    #url = contactrequest.get_admin_url()
    user = User.objects.get(id=comentario.post.autor.id)
    Notificacao.objects.create(title="Comentario", 
            content=comentario.comentario, user=user )

