from .models import Order
from django.forms import ModelForm, TextInput


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone']

    widgets = {
        "name": TextInput(attrs={
            'class': 'input_place',
            'name': 'name',
            'placeholder': 'Name',
            'data-max-length': "20",
            'data-min-length': "2",
            'id': "1"
        }),
        "email": TextInput(attrs={
            'class': 'input_place',
            'name': 'email',
            'placeholder': 'Email',
            'data-max-length': "50",
            'data-min-length': "6",
            'id': "2"
        }),
        "phone": TextInput(attrs={
            'class': 'input_place',
            'name': 'phone',
            'placeholder': 'Phone',
            'data-max-length': "20",
            'data-min-length': "9",
            'id': "3"
        })
    }
 