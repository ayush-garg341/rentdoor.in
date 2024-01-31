from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        help_texts = {
            "username": None,
        }

        labels = {"username": "Username", "password": "Password"}
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Email or username...",
                }
            ),
            "password": forms.PasswordInput(attrs={"placeholder": ""}),
        }


class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "username": "Username",
            "email": "Email",
            "password": "Password",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Email...",
                }
            ),
            "password": forms.PasswordInput(attrs={"placeholder": ""}),
        }
