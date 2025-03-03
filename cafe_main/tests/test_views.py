# from django.core.exceptions import ValidationError
# from orders.models import Order
# import pytest

# @pytest.mark.django_db
# def test_order_created_in_db(dishes_for_test):
#     """
#     Test if order recordered in DB.
#     """
#     order = Order.create_order(
#         table_number=2,
#         dishes=dishes_for_test)
#     order.count_total_price()
#     saved_order = Order.objects.get(pk=order.pk)
#     assert saved_order.dishes == dishes_for_test
#     assert saved_order.table_number == 2
#     assert saved_order.status_order == 'cooking'
#     assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)
#     order.dishes.append({"dish_name":"beefsteak", "price": 50.0})
#     order.count_total_price()
#     order.save()
#     saved_order = Order.objects.get(pk=order.pk)
#     assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)

# @pytest.mark.django_db
# def test_dish_added_in_order(dishes_for_test):
#     """
#     Test if new dish can be added in dish list and total price change correctly.
#     """
#     order = Order.create_order(
#         table_number=2,
#         dishes=dishes_for_test)
#     order.count_total_price()
#     saved_order = Order.objects.get(pk=order.pk)
#     assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)
#     order.dishes.append({"dish_name":"beefsteak", "price": 50.0})
#     order.count_total_price()
#     order.save()
#     saved_order = Order.objects.get(pk=order.pk)
#     assert saved_order.total_price == sum(dish['price'] for dish in dishes_for_test)
#     assert len(saved_order.dishes) == 3

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
