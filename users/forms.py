from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    username = forms.CharField(max_length=40)
    address = forms.CharField(max_length=300)
    postcode = forms.CharField(max_length=10)
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'postcode', 'password1', 'password2']
