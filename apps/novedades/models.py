from django.db import models
from django.utils import timezone


# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre

class Novedad(models.Model):
	nombre = models.CharField(max_length = 50)
	categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
	texto = models.TextField()
	imagen = models.ImageField(upload_to = 'novedades')
	author = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.nombre