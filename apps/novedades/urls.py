
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'novedades'


urlpatterns = [

	path('ALTA_N/', views.Alta_Novedad, name = 'cargar_n'),
	path('ALTA_C/', views.Alta_Categoria.as_view() , name = 'cargar_c'),
	path('Listar/', views.Listar , name = 'listar'),
	path('post/<int:pk>/', views.post_detalle, name='post_detalle'),
	path('post/<int:pk>/edit/', views.Alta_edit, name='Alta_edit'),
	re_path(r'^post/(?P<pk>\d+)/comentar/$', views.agregar_comentario, name='agregar_comentario'),
	path('filtrar/', views.filtrar, name = 'filtrar'),
	path('filtro/', views.NovedadListView.as_view(), name='filtro'),


 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)