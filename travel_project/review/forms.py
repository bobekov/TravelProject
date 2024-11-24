from django import forms
from travel_project.review.models import Review


class AddReview(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', )

