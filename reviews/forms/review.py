from django.forms import ModelForm, ValidationError
from django import forms
from reviews.models.review import Reviews
import re


class CreateReviewForm(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        pin_code = cleaned_data.get("pin_code")
        is_valid = bool(re.search(r"^[1-9][0-9]{5}$", pin_code))
        if not is_valid:
            raise ValidationError("Please enter valid pin code")

        description = cleaned_data.get("description")
        if not len(description) >= 400:
            raise ValidationError("Please write atleast 400 chars in description")

        return cleaned_data

    class Meta:
        model = Reviews
        fields = [
            "title",
            "description",
            "city",
            "state",
            "pin_code",
            "address_line_1",
            "address_line_2",
        ]
        labels = {
            "description": "Description",
            "title": "Title",
            "address_line_1": "Address Line One",
            "address_line_2": "Address Line Two",
        }
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Share your experience...",
                    "required": "required",
                }
            ),
        }


class SearchReviewForm(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        pin_code = cleaned_data.get("pin_code")
        locality = cleaned_data.get("locality")

        if not pin_code and not locality:
            raise ValidationError("Please enter either pincode or locality")

        return cleaned_data

    pin_code = forms.CharField(max_length=100, required=False, label="Pincode")
    locality = forms.CharField(max_length=100, required=False, label="Locality")
