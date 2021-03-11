
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'novedades'



urlpatterns = [

	path('ALTA_N/', views.Alta_Novedad.as_view() , name = 'cargar_n'),
	path('ALTA_C/', views.Alta_Categoria.as_view() , name = 'cargar_c'),
	path('Listar/', views.Listar.as_view() , name = 'listar'),
	path('f_categoria/', views.Filtrar_categoria.as_view() , name = 'f_categoria'),

 
    
]
