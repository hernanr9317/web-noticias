
from django.urls import path
from . import views


app_name = 'usuarios'


urlpatterns = [

	
	path('Registro/', views.Registrar_usuario.as_view() , name ="registrar_usuario"),
	path('Listar_u/', views.Listar_usuario , name = 'listar_usuarios')
 
    
]
