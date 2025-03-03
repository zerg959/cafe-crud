from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from django.db.models.functions import Cast
from django.db.models import FloatField
from .serializers import OrderSerializer
from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    """
    Order viewset for CRUD-operations.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=["get"])
    def get_order_by_table(self, request):
        """
        Filter all orders by table number.
        """
        table_number = request.query_params.get("table_number")
        if table_number is None or int(table_number) <= 0:
            return Response({"error": "Enter positive table number."}, status=400)
        try:
            table_number = int(table_number)
        except (ValueError, TypeError):
            return Response(
                {"error": "Invalid input: Table number must be an integer."}, status=400
            )
        queryset = Order.objects.filter(table_number=table_number)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

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
