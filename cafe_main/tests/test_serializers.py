import pytest
from api_cafe.serializers import OrderSerializer


def test_order_serializer(order_data):
    """
    Test if serializer read data.
    """
    serializer = OrderSerializer(data=order_data)
    assert serializer.is_valid()
    order_data["total_price"] = (
        f"{order_data['total_price']:.2f}"  # modify format to String
    )
    assert serializer.data == order_data


@pytest.mark.django_db
def test_serialized_order_created(order_data):
    """
    Test if serializer create serialized object.
    """
    serializer = OrderSerializer(data=order_data)
    assert serializer.is_valid()

    instance = serializer.save()
    assert instance.table_number == order_data["table_number"]
    assert instance.dishes == order_data["dishes"]
    assert len(instance.dishes) == len(order_data["dishes"])
    assert instance.status_order == 'cooking'
    assert instance.total_price == sum(dish['price'] for dish in instance.dishes)
