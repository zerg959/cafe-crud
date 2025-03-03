from typing import List, Dict, Any, Tuple
from django.db import models
from django.core.exceptions import ValidationError
import json


class Order(models.Model):
    """
    Order model.
    Attr:
    - table_number: table number;
    - items: ordered dishes;
    - total_price: total price of all ordered dishes;
    - status_order: possible statuses of order;
    Methods:
    - count_total_price: calculate total price of all dishes in order;
    - save: record new data in object attr.
    """
    STATUSES_ORDERS: Tuple = (
        ("cooking", "Cooking"),
        ("ready", "Ready"),
        ("paid", "Paid"),
    )
    table_number: int = models.PositiveIntegerField(
        verbose_name="table number"
        )
    dishes: List[dict] = models.JSONField(
        verbose_name="list of dishes",
        default=list
    )
    total_price: float = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="total price",
        default=0,
        )
    status_order: str = models.CharField(
        max_length=20,
        verbose_name="order status",
        choices=STATUSES_ORDERS,
        default="cooking"
    )

    def count_total_price(self) -> None:
        """
        Count total price of the order.
        """
        if not self.dishes or not isinstance(self.dishes, list):
            self.total_price = 0  # set total price to zero.
            return

        self.total_price = sum(
            dish.get("price", 0)
            for dish in self.dishes if isinstance(dish, dict)
            )

    def save(self, *args, **kwargs) -> None:
        """
        Save Order-object in DB.
        """
        if isinstance(self.dishes, str):  # Check if dishes is String
            try:
                self.dishes = json.loads(self.dishes)
            except json.JSONDecodeError:
                raise ValidationError(
                    "Invalid JSON format for 'dishes' field."
                    )
        if isinstance(self.total_price, str):
            try:
                self.total_price = Decimal(self.total_price)
            except ValueError:
                raise ValidationError("Invalid format for 'total_price'.\
                                      Must be a number.")

        if not isinstance(self.dishes, list):
            raise ValidationError(
                "The 'dishes' field must be a list of dictionaries."
                )
        self.count_total_price()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Order {self.id}, Table: {self.table_number},\
          Total price: {self.total_price}'
