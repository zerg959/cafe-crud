import json
from django import forms

class OrderForm(forms.Form):
    table_number = forms.IntegerField(label="Table Number")
    dishes = forms.CharField(label="Dishes (JSON)")

    def clean_dishes(self):
        dishes = self.cleaned_data['dishes']
        try:
            dishes_list = json.loads(dishes)
            if not isinstance(dishes_list, list):
                raise forms.ValidationError("Dishes must be a list.")
            for item in dishes_list:
                if not isinstance(item, dict):
                    raise forms.ValidationError("Each item in dishes must be a dictionary.")
                if not all(key in item for key in ["dish_name", "price"]):
                    raise forms.ValidationError("Each dish must have 'dish_name' and 'price' keys.")
            return dishes
        except json.JSONDecodeError:
            raise forms.ValidationError("Invalid JSON format.")