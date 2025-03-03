from orders.models import Order
from django.core.exceptions import ValidationError
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


@pytest.mark.django_db
def test_order_created_in_db(dishes_for_test):
    """
    Test if order recordered in DB.
    """
    order = Order.create_order(
        table_number=2,
        dishes=dishes_for_test)
    order.count_total_price()
    saved_order = Order.objects.get(pk=order.pk)
    assert saved_order.dishes == dishes_for_test
    assert saved_order.table_number == 2
    assert saved_order.status_order == 'cooking'
    assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)
    order.dishes.append({"dish_name":"beefsteak", "price": 50.0})
    order.count_total_price()
    order.save()
    saved_order = Order.objects.get(pk=order.pk)
    assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)

@pytest.mark.django_db
def test_dish_added_in_order(dishes_for_test):
    """
    Test if new dish can be added in dish list and total price change correctly.
    """
    order = Order.create_order(
        table_number=2,
        dishes=dishes_for_test)
    order.count_total_price()
    saved_order = Order.objects.get(pk=order.pk)
    assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)
    order.dishes.append({"dish_name":"beefsteak", "price": 50.0})
    order.count_total_price()
    order.save()
    saved_order = Order.objects.get(pk=order.pk)
    assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)
    assert len(saved_order.dishes) == 3

@pytest.mark.django_db
def test_order_status_changed(order_for_test):
    order = order_for_test
    order.count_total_price()
    order.save()
    saved_order = Order.objects.get(pk=order.pk)
    assert saved_order.status_order == 'cooking'
    order.change_status('ready')
    order.save()
    saved_order = Order.objects.get(pk=order.pk)
    assert saved_order.status_order == 'ready'
    with pytest.raises(ValidationError) as err_info:
        order.change_status('other')
    assert 'Unknown status' in err_info.value.messages
