import pytest
from django.conf import settings
from orders.models import Order
from api_cafe.serializers import OrderSerializer
# from django.contrib.auth.models import User
import os

@pytest.fixture(scope="session")
def use_in_memory_db():
    """
    DB fixture.
    """
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }

@pytest.fixture
def dishes_for_test():
    """
    Dishes for order fixture.
    """
    dishes_for_test = [{'name': 'Pizza', 'price': 12.50}, {'name': 'Pasta', 'price': 10.00}]
    return dishes_for_test


@pytest.fixture
def order_data():
    return {
        "table_number": 2,
        "dishes": [
            {
                "dish_name": "Beefsteak",
                "price": 100.00,
             },
            {
                "dish_name": "Side Salad",
                "price": 50.00,
            },
              ],
        "total_price": 150.00,
        "status_order": "cooking",
    }
