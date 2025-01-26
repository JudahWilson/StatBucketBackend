from django_filters import rest_framework as filters
from webapp.models import *

def filter_generator(filter_instance):
    '''
    Set a filter for each field in the model
    '''
    for field_name in filter_instance.Meta.model._meta.fields:
            if isinstance(field_name, models.CharField) or isinstance(field_name, models.TextField):
                # For character-based fields, add icontains and iexact filters
                filter_instance.filters[f'{field_name.name}__icontains'] = filters.CharFilter(field_name=field_name.name, lookup_expr='icontains')
                filter_instance.filters[f'{field_name.name}'] = filters.CharFilter(field_name=field_name.name, lookup_expr='iexact')
            elif isinstance(field_name, models.ForeignKey):
                # For foreign key fields, add exact filter
                filter_instance.filters[f'{field_name.name}'] = filters.NumberFilter(field_name=field_name.name, lookup_expr='exact')
            elif isinstance(field_name, models.IntegerField) or isinstance(field_name, models.FloatField) or isinstance(field_name, models.DecimalField):
                # For integer fields, add exact filter
                filter_instance.filters[f'{field_name.name}'] = filters.NumberFilter(field_name=field_name.name, lookup_expr='exact')
                filter_instance.filters[f'{field_name.name}__gte'] = filters.NumberFilter(field_name=field_name.name, lookup_expr='gte')
                filter_instance.filters[f'{field_name.name}__lte'] = filters.NumberFilter(field_name=field_name.name, lookup_expr='lte')
                filter_instance.filters[f'{field_name.name}__gt'] = filters.NumberFilter(field_name=field_name.name, lookup_expr='gt')
                filter_instance.filters[f'{field_name.name}__lt'] = filters.NumberFilter(field_name=field_name.name, lookup_expr='lt')
            elif isinstance(field_name, models.BooleanField):
                # For boolean fields, add exact filter
                filter_instance.filters[f'{field_name.name}'] = filters.BooleanFilter(field_name=field_name.name, lookup_expr='exact')
            elif isinstance(field_name, models.DateTimeField) or isinstance(field_name, models.DateField):
                # For date and datetime fields, add exact filter
                filter_instance.filters[f'{field_name.name}'] = filters.DateFilter(field_name=field_name.name, lookup_expr='exact')
                filter_instance.filters[f'{field_name.name}__gte'] = filters.DateFilter(field_name=field_name.name, lookup_expr='gte')
                filter_instance.filters[f'{field_name.name}__lte'] = filters.DateFilter(field_name=field_name.name, lookup_expr='lte')
                filter_instance.filters[f'{field_name.name}__gt'] = filters.DateFilter(field_name=field_name.name, lookup_expr='gt')
                filter_instance.filters[f'{field_name.name}__lt'] = filters.DateFilter(field_name=field_name.name, lookup_expr='lt')

class UniversalFilter(filters.FilterSet):
    '''
    The filter set for API views that automatically create a filter for every field in the model
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        filter_generator(self)

    @classmethod
    def create_filter(cls, model):
        Meta = type('Meta', (object,), {'model': model, 'fields': []})
        
        # Create a new filter class with this Meta class
        attrs = {'Meta': Meta}
        filter_cls = type(f'{model.__name__}Filter', (cls,), attrs)
        return filter_cls
