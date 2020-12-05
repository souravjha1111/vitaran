from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Orders
CHOICES =( 
    ("1", "yes"), 
    ("0", "No"), 
) 
class postorderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['user','order_to', 'order_from','approx_weight','approx_size',
                'description','order_image','bidding_choice']

