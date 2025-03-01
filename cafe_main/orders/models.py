# https://ru.hexlet.io/courses/python-django-orm/lessons/annotation/theory_unit 

from typing import List, Dict, Any
from django.db import models
from django.core.exceptions import ValidationError

class Order(models.Model):
    """
    Order model.
    Attr:
    - table_number: table number;
    - items: ordered dishes;
    - total_price: total price of all ordered dishes;
    - status_order: possible stauses of order;
    Methods:
    - count_total_price: calculate total price of all dishes in order;
    - save: record new data in object attr.
    """
    STATUSES_ORDERS = (
        ("cooking", "Cooking"),
        ("ready", "Ready"),
        ("paid", "Paid"),
    )
    table_number: int = models.PositiveIntegerField(
        verbose_name="table number"
        )
    items: List[dict] = models.JSONField(
        verbose_name="list of dishes",
        default=[]
    )
    total_price: float = models.DecimalField(
        decimal_places=2, 
        verbose_name="total price"
        )
    status_order: str = models.CharField(
        verbose_name="order status",
        choices=STATUSES_ORDERS,
        default="Cooking"
    )
    def count_total_price(self) -> None:
        """
        Count total price of the order.
        """
        if not self.items:
            raise ValidationError('No dishes in order!')
        
        self.total_price =  sum(item["price"] for item in self.items)
        self.save()

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        self.count_total_price()
    
    def __str__(self) -> str:
        return f'Order {self.id}, Table: {self.table_number}'
