from django.forms import ModelForm
from .models import checkout
class checkoutform(ModelForm):
    class Meta:
        model = checkout
        fields = [
            'city',
            'address',
            'postcode',
            'firstname',
            'lastname',
            'phone_number',
            'house_number',
        ]