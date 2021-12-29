from django_filters import rest_framework as filters
from .models import Droid


# We create filters for each field we want to be able to filter on
class DroidFilter(filters.FilterSet):
    descricao = filters.CharFilter(lookup_expr='icontains')
    endereco = filters.CharFilter(lookup_expr='icontains')
    contato = filters.NumberFilter()
    contato__gt = filters.NumberFilter(field_name='contato', lookup_expr='gt')
    contato__lt = filters.NumberFilter(field_name='contato', lookup_expr='lt')
    anunciante__username = filters.CharFilter(lookup_expr='icontains')
    status = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Droid
        fields = ['descricao', 'endereco', 'contato', 'contato__gt', 'contato__lt', 'anunciante__username', 'status']

