from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import FloatField
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import OrderSerializer
from orders.models import Order
from orders.filtersets import OrderFilter


class OrderViewSet(viewsets.ModelViewSet):
    """
    Order viewset for CRUD-operations.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = OrderFilter
    ordering_fields = ["table_number", "status_order"]

    @action(detail=False, methods=["get"], url_path="revenue")
    def calculate_revenue(self, request):
        """
        Calculate total revenue for orders with status 'paid'.
        """
        # Filter orders with paid-status.
        paid_orders = Order.objects.filter(status_order="paid")

        # Rewrite total_price to Float.
        total_revenue = (
            paid_orders.annotate(
                numeric_total_price=Cast("total_price", output_field=FloatField())
            ).aggregate(total=Sum("numeric_total_price"))["total"]
            or 0
        )
        # Return result.
        return Response({"total_revenue": total_revenue})

    # @action(detail=False, methods=["get"], url_path="order_status")
    # def get_orders_by_status(self, request):
    #     """
    #     Filter orders by status: 'cooking', 'paid', 'ready'.
    #     """
    #     # Filter orders with selected status.
    #     status_order = request.query_params.get("status_order")
    #     if not status_order:
    #         return Response({"error": "status_order parameter is required"},
    #                     status=status.HTTP_400_BAD_REQUEST)
    #     if status_order not in dict(Order.STATUSES_ORDERS).keys():
    #         raise ValidationError({"error": "Invalid status_order value (not 'cooking', 'paid', 'ready')"})
    #     queryset = Order.objects.filter(status_order=status_order)
    #     serializer = OrderSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # @action(detail=False, methods=["get"])
    # def get_order_by_table(self, request):
    #     """
    #     Filter all orders by table number.
    #     """
    #     table_number = request.query_params.get("table_number")
    #     if table_number is None or int(table_number) <= 0:
    #         return Response({"error": "Enter positive table number."}, status=400)
    #     try:
    #         table_number = int(table_number)
    #     except (ValueError, TypeError):
    #         return Response(
    #             {"error": "Invalid input: Table number must be an integer."}, status=400
    #         )
    #     queryset = Order.objects.filter(table_number=table_number)
    #     serializer = OrderSerializer(queryset, many=True)
    #     return Response(serializer.data)
