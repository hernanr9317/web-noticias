
from django import forms
from .models import Categoria, Novedad
from django.forms.widgets import SelectDateWidget


class Formulario_Alta_Novedad(forms.ModelForm):

	class Meta:
		model = Novedad
		fields = '__all__'

class Formulario_Alta_Categoria(forms.ModelForm):

	class Meta:
		model = Categoria
		fields = '__all__'

class Formulario_Fecha(forms.Form):
	Fecha = forms.DateField(widget= SelectDateWidget())


class Formulario_filtro(forms.ModelForm):

	class Meta:
		model = Novedad
		fields = ['categoria']