from orders.models import Order


def test_order_created():
    new_order = Order(
        table_number=1,
        items=[
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
    assert len(new_order.items) == 2
    assert new_order.items[0]["dish_name"] == "Beefsteak"
    assert new_order.items[1]["dish_name"] == "Side Salad"
