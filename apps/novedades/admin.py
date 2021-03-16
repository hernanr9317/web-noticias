from django.contrib import admin

# Register your models here.
from .models import Novedad
from .models import Categoria
from .models import  Comentario

admin.site.register(Comentario)
admin.site.register(Novedad)
admin.site.register(Categoria)