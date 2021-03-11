from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Listar_usuario(request):

	usuarios = Usuario.objects.all()
	ctx = {}
	ctx['p'] = usuarios
	return render(request, 'usuarios/listar_usuarios.html',ctx)


class Registrar_usuario(CreateView):
	model = 'Usuario'
	form_class = RegistroUsuarioForm
	template_name = 'usuarios/signup.html'
	success_url = reverse_lazy('home')