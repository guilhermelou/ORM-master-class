# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User,related_name=u'User_Profile')
	birthDate = models.DateField(u'Data de Nascimento', null=True)
	gender = models.NullBooleanField(u'Sexo',null=True)
	#profileImg = models.ImageField(u'Imagem do Perfil',null=True)

