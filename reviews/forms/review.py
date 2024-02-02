from django.forms import ModelForm
from django import forms
from reviews.models.review import Review


class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["title", "description"]
        labels = {"description": "Description", "title": "Title"}
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Add a description...",
                    "required": "required",
                }
            ),
            "title": forms.TextInput(attrs={"placeholder": "", "required": "required"}),
        }
