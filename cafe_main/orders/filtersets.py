import django_filters
from .models import Order


class OrderFilter(django_filters.FilterSet):
    table_number = django_filters.NumberFilter(
        field_name="table_number", lookup_expr="exact"
    )
    status_order = django_filters.ChoiceFilter(
        choices=Order.STATUSES_ORDERS, field_name="status_order", lookup_expr="exact"
    )

    class Meta:
        model = Order
        fields = ["table_number", "status_order"]
