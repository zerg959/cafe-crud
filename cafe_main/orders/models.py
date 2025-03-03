# https://ru.hexlet.io/courses/python-django-orm/lessons/annotation/theory_unit 

from typing import List, Dict, Any, Tuple
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
        default=[]
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

    def change_status(self, new_status):
        # statuses = STATUSES_ORDERS
        if new_status != self.status_order:
            if new_status not in dict(self.STATUSES_ORDERS).keys():
                raise ValidationError('Unknown status')
            self.status_order = new_status
            self.save()
            return True
        return False
        
        


    def count_total_price(self) -> None:
        """
        Count total price of the order.
        """
        if not self.dishes:
            raise ValidationError('No dishes in order!')

        self.total_price = sum(dish["price"] for dish in self.dishes)

    def save(self, *args, **kwargs) -> None:
        """
        Save Order-object in DB.
        """
        super().save(*args, **kwargs)

    @classmethod
    def create_order(cls, table_number, dishes):
        """
        Create Order object in DB.
        """
        new_order = cls(
            table_number=table_number,
            dishes=dishes,
            )
        new_order.count_total_price()
        new_order.save()
        return new_order


    def __str__(self) -> str:
        return f'Order {self.id}, Table: {self.table_number}, Total price: {self.total_price}'
