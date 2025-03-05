from django.core.exceptions import ValidationError
from orders.models import Order
from decimal import Decimal
import pytest


@pytest.mark.django_db
def test_count_total_price_with_dishes(order_for_test):
    """
    Test total price calculation with a list of dishes.
    """
    order_for_test.count_total_price()
    assert order_for_test.total_price == Decimal('22.50')


@pytest.mark.django_db
def test_count_total_price_with_empty_lidt_dishes(order_for_test):
    """
    Test total price calculation with a list of dishes.
    """
    order_for_test.dishes = []
    assert order_for_test.total_price == Decimal('0.00')


@pytest.mark.django_db
def test_count_total_price_with_empty_list_dishes(order_for_test):
    """
    Test total price calculation with a empty list of dishes and.
    """
    order_for_test.dishes = []
    order_for_test.count_total_price()
    assert order_for_test.total_price == Decimal('0.00')
    order_for_test.dishes = 'any string'
    order_for_test.count_total_price()
    assert order_for_test.total_price == Decimal('0.00')


@pytest.mark.django_db
def test_save_valid_json_dishes():
    """
    Test if save() successfully parses a valid JSON string in 'dishes'.
    """
    order = Order(table_number=1, dishes='[{"name": "Tea", "price": 3.00}]')
    order.save()  # Sve serialized object into DB.
    assert isinstance(order.dishes, list)
    assert len(order.dishes) == 1
    assert order.dishes[0]['name'] == 'Tea'
    assert order.dishes[0]['price'] == 3.00


@pytest.mark.django_db
def test_invalid_json_dishes_raise_e():
    """
    Test error raises if order has invalid JSON string in 'dishes'.
    """
    with pytest.raises(ValidationError) as excinfo: 
        order = Order(table_number=1, dishes="string")
        order.save()  # Sve serialized object into DB.
    assert str(excinfo.value) == '["Invalid JSON format for \'dishes\' field."]'