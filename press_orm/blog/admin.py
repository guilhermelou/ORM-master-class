from django.contrib import admin
from blog.models import Notificacao, Post, Comentario,Categoria
# Register your models here.

admin.site.register(Notificacao)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Categoria)