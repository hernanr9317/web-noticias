
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegistroUsuarioForm(UserCreationForm):

	class Meta:
		model = Usuario
		fields = ['username','email','first_name','last_name','password1','password2']

		
	

