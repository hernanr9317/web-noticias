import django_filters
from .models import Novedad
from django.forms.widgets import SelectDateWidget
from django.utils import timezone

class PostFilter(django_filters.FilterSet):

	CHOICES = (
			('descendente', 'Posts mas recientes'),
			('ascendente', 'Posts antiguos')
		)

	ordering = django_filters.ChoiceFilter(label='Fecha', choices=CHOICES, method='filter_by_order')


	class Meta:
		model = Novedad
		fields = ['categoria']

	def filter_by_order(self, queryset, name, value):
		expression = 'published_date' if value == 'ascendente' else '-published_date'
		return queryset.order_by(expression)
	