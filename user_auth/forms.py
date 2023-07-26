from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User registation form, simply containing username and password, but added first_name field
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=120)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']