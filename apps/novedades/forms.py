
from django import forms
from .models import *
from django.forms.widgets import SelectDateWidget


class Formulario_Alta_Novedad(forms.ModelForm):

	class Meta:
		model = Novedad
		fields =  ['titulo','categoria','texto','imagen']

class Formulario_Alta_Categoria(forms.ModelForm):

	class Meta:
		model = Categoria
		fields = '__all__'


class Formulario_filtro(forms.ModelForm):

	class Meta:
		model = Novedad
		fields = ['categoria']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['texto']


