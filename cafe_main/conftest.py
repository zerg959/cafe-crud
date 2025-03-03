import pytest
from django.conf import settings
from orders.models import Order
# from django.contrib.auth.models import User
import os

@pytest.fixture(scope="session")  # autouse=True означает, что она будет автоматически использоваться для всех тестов
def use_in_memory_db():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }

@pytest.fixture
def dishes_for_test():
    dishes_for_test = [{'name': 'Pizza', 'price': 12.50}, {'name': 'Pasta', 'price': 10.00}]
    return dishes_for_test

@pytest.fixture
def order_for_test():
    dishes = [{'name': 'Pizza', 'price': 12.50}, {'name': 'Pasta', 'price': 10.00}]
    order = Order.create_order(
        table_number=2,
        dishes=dishes)
    return order