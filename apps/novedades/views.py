from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import template
from  django.http import HttpResponse
from .filters import PostFilter

# Create your views here.




def Listar(request):
    novedad= Novedad.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'novedades/listar.html', {'novedad':novedad})

def post_detalle(request, pk):
    novedad = get_object_or_404(Novedad, pk=pk)
    return render(request, 'novedades/post_detalle.html', {'novedad': novedad})

def filtrar(request):
    return render(request, 'novedades/f_categoria.html')

@login_required
def Alta_Novedad(request):
    if request.method == "POST":
        form = Formulario_Alta_Novedad(request.POST, request.FILES)
        if form.is_valid():
            novedad = form.save(commit=False)
            novedad.author = request.user
            novedad.published_date = timezone.now()
            novedad.save()
            return redirect('novedades:post_detalle', pk=novedad.pk)
    else:
        form = Formulario_Alta_Novedad()
    return render(request,'novedades/alta_novedad.html', {'form': form})

def Alta_edit(request, pk):
    novedad = get_object_or_404(Novedad, pk=pk)
    if request.method == "POST":
        form = Formulario_Alta_Novedad(request.POST, request.FILES, instance=novedad)
        if form.is_valid():
            novedad = form.save(commit=False)
            novedad.author = request.user
            novedad.published_date = timezone.now()
            novedad.save()
            return redirect('novedades:post_detalle', pk=novedad.pk)
    else:
        form = Formulario_Alta_Novedad(instance=novedad)
    return render(request, 'novedades/alta_novedad.html', {'form': form})

class Alta_Categoria(LoginRequiredMixin, CreateView):
	model = 'Categoria'
	form_class = Formulario_Alta_Categoria
	template_name = 'novedades/alta_categoria.html'
	success_url = reverse_lazy('home')

@login_required
def agregar_comentario(request, pk):
    novedad = get_object_or_404(Novedad, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.novedad = novedad
            comentario.author = request.user
            comentario.post_id = novedad.pk
            comentario.save()
            return redirect('novedades:post_detalle', pk=novedad.pk)
    else:
        form = ComentarioForm()
    return render(request, 'novedades/agregar_comentario.html', {'form': form})


class NovedadListView(ListView):
    model = Novedad
    template_name = 'novedades/filtro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset().order_by('-published_date'))
        return context



