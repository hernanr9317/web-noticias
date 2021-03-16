from django.db import models
from django.utils import timezone


# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombre

class Novedad(models.Model):
	titulo = models.CharField(max_length = 200)
	categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
	texto = models.TextField()
	imagen = models.ImageField(upload_to = 'novedades')
	author = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
	published_date = models.DateTimeField()

	
	def __str__(self):
		return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey('novedades.Novedad', on_delete=models.CASCADE, related_name='comentarios')
    author = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text

class Filtro_categoria(models.Model):
	categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)