from django.forms import ModelForm
from django import forms
from reviews.models.review import Reviews


class CreateReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = [
            "title",
            "description",
            "city",
            "state",
            "pin_code",
            "country",
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
    pin_code = forms.CharField(max_length=100, required=False, label="Pincode")
    locality = forms.CharField(max_length=100, required=False, label="Locality")
