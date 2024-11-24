from django import forms
from travel_project.country.models import Country


class AddCountry(forms.ModelForm):
    class Meta:
        model = Country
        exclude = ('user', )

        widgets = {
            "description": forms.Textarea(attrs={
                "placeholder": "Make a description of the country."
            }),
            "population": forms.TextInput(attrs={
                "placeholder": "Population in millions."
            }),
            "flag": forms.TextInput(attrs={
                "placeholder": "URL field: http//..."
            }),
        }


