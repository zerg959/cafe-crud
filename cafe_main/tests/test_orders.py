from orders.models import Order
import pytest


def test_order_created():
    """
    Test if object created in ORM.
    """
    new_order = Order(
        table_number=1,
        dishes=[
            {
                "dish_name": "Beefsteak",
                "price": 100,
                "status_order": "cooking"
             },
            {
                "dish_name": "Side Salad",
                "price": 50,
                "status_order": "cooking"
            },
              ])
    assert new_order is not None
    assert isinstance(new_order, Order)
    assert len(new_order.dishes) == 2
    assert new_order.dishes[0]["dish_name"] == "Beefsteak"
    assert new_order.dishes[1]["dish_name"] == "Side Salad"
