from django.forms import ModelForm
from django import forms
from reviews.models.review import Reviews


class CreateReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = [
            "title",
            "description",
            "house_num",
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
            "house_num": "House No",
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
