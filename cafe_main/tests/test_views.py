from django.core.exceptions import ValidationError
from orders.models import Order
import pytest


# @pytest.mark.django_db
# def test_dish_added_in_order(order_for_test, dishes_for_test):
#     """
#     Test if new dish can be added in dish list and total price change correctly.
#     """
#     order = order_for_test()
#     start_len = len(order.dishes)
#     new_dishes = dishes_for_test()
#     order.dishes.append(new_dishes)
#     final_len = len(order.dishes)
# #     order.count_total_price()
# #     order.save()
# #     saved_order = Order.objects.get(pk=order.pk)
# #     assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)
#     assert (len(order_for_test.dishes) + len(dishes_for_test())) == final_len

# @pytest.mark.django_db
# def test_order_status_changed(order_for_test):
#     """
#     Test if change_status can change status with valid values and raise error otherwise.
#     """
#     order = order_for_test
#     order.count_total_price()
#     order.save()
#     saved_order = Order.objects.get(pk=order.pk)
#     assert saved_order.status_order == 'cooking'
#     order.change_status('ready')
#     order.save()
#     saved_order = Order.objects.get(pk=order.pk)
#     assert saved_order.status_order == 'ready'
#     with pytest.raises(ValidationError) as err_info:
#         order.change_status('other')
#     assert 'Unknown status' in err_info.value.messages
