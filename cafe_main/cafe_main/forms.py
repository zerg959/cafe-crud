import json
from django import forms
from orders.models import Order

class OrderForm(forms.Form):
    table_number = forms.IntegerField(label="Table Number")
    dishes = forms.CharField(label="Dishes (JSON)", widget=forms.Textarea)
    status_order = forms.ChoiceField(
        label="Status Order",
        choices=Order.STATUSES_ORDERS,
        required=False
    )

    def clean_table_number(self):
        table_number = self.cleaned_data['table_number']
        if table_number <= 0:
            raise forms.ValidationError("Table number must be positive.")
        return table_number

    def clean_dishes(self):
        dishes_string = self.cleaned_data['dishes'] # it's string
        try:
            dishes_list = json.loads(dishes_string)  # Try to parse string to JSON-list

            if not isinstance(dishes_list, list):
                raise forms.ValidationError("Dishes must be a list.")

            for item in dishes_list:
                if not isinstance(item, dict):
                    raise forms.ValidationError("Each item in dishes must be a dictionary.")

                if not all(key in item for key in ["dish_name", "price"]):
                    raise forms.ValidationError("Each dish must have 'dish_name' and 'price' keys.")

                try:
                    float(item['price'])  # check if the price can be convert to float
                except ValueError:
                    raise forms.ValidationError("Dish price must be a number.")

            return json.dumps(dishes_list) # returns JSON to the dishes, not python-list

        except json.JSONDecodeError as e:
            raise forms.ValidationError(f"Invalid JSON format: {e}")
