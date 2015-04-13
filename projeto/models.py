# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
	titulo = models.CharField(max_length=140)
	descricao = models.CharField(max_length=140)
	conteudo = models.TextField()
	slug = models.SlugField()      # caminho da url do post
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	autor = models.ForeignKey(User)         # cada post podera ter apenas um usuario
	link = models.URLField(blank=True)		# link opcional que o autor do post pode colocar
	link_descricao = models.CharField(max_length=140, blank=True)

	# classe para tratar a ordenação de post antigos
	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('projeto.views.getpost', args=[self.slug])
