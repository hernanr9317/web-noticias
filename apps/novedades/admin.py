from django.contrib import admin

# Register your models here.
from .models import Novedad
from .models import Categoria

admin.site.register(Novedad)
admin.site.register(Categoria)