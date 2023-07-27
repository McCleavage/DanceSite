from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """This class represents an extension of the stock Django user form

        :param CharField first_name: The user's first name
        :param class Meta: Meta class data storing user model and all fields

    """
    first_name = forms.CharField(max_length=120)

    class Meta:
        """This class represents some of the metadata of a user

            :param User model: The model of the user
            :param list fields:List referring to all fields

        """
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']