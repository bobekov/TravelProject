from django import forms
from travel_project.destination.models import Destination


class AddDestination(forms.ModelForm):
    class Meta:
        model = Destination
        exclude = ('user', )

        widgets = {
            "attractions": forms.Textarea(attrs={
                "placeholder": "What attractions can be seen in the region."
            }),
            "image": forms.TextInput(attrs={
                "placeholder": "URL field: http//..."
            }),
            "best_time_to_visit": forms.TextInput(attrs={
                "placeholder": "e.g. season or month"
            }),
        }