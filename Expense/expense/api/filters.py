import django_filters
from .models import *

class ExpenseFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr='lte')
    category = django_filters.ChoiceFilter(choices=Expense.CATEGORY_CHOICES)
    product = django_filters.CharFilter(field_name='product__name', lookup_expr='iexact')

    class Meta:
        model = Expense
        fields = ['start_date', 'end_date', 'category', 'product']