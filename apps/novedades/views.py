from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Categoria, Novedad
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin


class Listar(ListView):
	model = Novedad
	template_name= 'novedades/listar.html'


class Filtrar_categoria(ListView):
	model = Novedad
	template_name= 'novedades/f_categoria.html'

	def get_queryset(self):
		query=super(Filtrar_categoria, self).get_queryset()
		return query.filter(categoria_id=1)



class Alta_Novedad(LoginRequiredMixin, CreateView):
	model = 'Novedad'
	form_class = Formulario_Alta_Novedad
	template_name = 'novedades/alta_novedad.html'
	success_url = reverse_lazy('home')

class Alta_Categoria(LoginRequiredMixin, CreateView):
	model = 'Categoria'
	form_class = Formulario_Alta_Categoria
	template_name = 'novedades/alta_categoria.html'
	success_url = reverse_lazy('home')
