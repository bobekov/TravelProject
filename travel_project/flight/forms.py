from django import forms

from travel_project.flight.models import Flight


class AddFlight(forms.ModelForm):
    class Meta:
        model = Flight
        exclude = ('user',)

        widgets = {
            "airlines_logo": forms.TextInput(attrs={
                "placeholder": "URL field: http//..."
            }),
            "destinations": forms.TextInput(attrs={
                "placeholder": "City, Country"
            }),
            'departure_time': forms.DateTimeInput(attrs={
                "type": "datetime-local"
            }),
            "arrival_time": forms.DateTimeInput(attrs={
                'type': "datetime-local"
            }),
            "price": forms.TextInput(attrs={
                "placeholder": "Price in Euro"
            }),
        }
