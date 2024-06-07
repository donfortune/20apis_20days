import django_filters
from .models import *
from django.utils import timezone
from datetime import timedelta

class ExpenseFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr='lte')
    category = django_filters.ChoiceFilter(choices=Expense.CATEGORY_CHOICES)
    product = django_filters.CharFilter(field_name='product__name', lookup_expr='iexact')

    class Meta:
        model = Expense
        fields = ['start_date', 'end_date', 'category', 'product']


class ExpenseFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category', lookup_expr='iexact')  # Make category case-insensitive
    product = django_filters.CharFilter(field_name='product__name', lookup_expr='iexact')

    past_week = django_filters.BooleanFilter(method='filter_past_week')
    last_month = django_filters.BooleanFilter(method='filter_last_month')
    last_3_months = django_filters.BooleanFilter(method='filter_last_3_months')

    class Meta:
        model = Expense
        fields = ['start_date', 'end_date', 'category', 'product', 'past_week', 'last_month', 'last_3_months']


    def filter_past_week(self, queryset, name, value):
        if value:
            return queryset.filter(created_at__gte=timezone.now() - timedelta(days=7))
        return queryset

    def filter_last_month(self, queryset, name, value):
        if value:
            return queryset.filter(created_at__gte=timezone.now() - timedelta(days=30))
        return queryset

    def filter_last_3_months(self, queryset, name, value):
        if value:
            return queryset.filter(created_at__gte=timezone.now() - timedelta(days=90))
        return queryset