from django.forms import ModelForm, ValidationError
from django import forms
from django.contrib.auth.models import User
from app_users.models.profile import Profile


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

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

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
                attrs={"placeholder": "", "required": "required"}
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "username": forms.TextInput(
                attrs={"placeholder": "", "required": "required"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "Email...", "required": "required"}
            ),
            "password": forms.PasswordInput(
                attrs={"placeholder": "", "required": "required"}
            ),
        }


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["job_title"]
        labels = {"job_title": "Job Title"}
        widgets = {
            "job_title": forms.TextInput(
                attrs={"placeholder": "", "required": "required"}
            ),
        }
