from django import forms

from travel_project.room.models import Room


class AddRoom(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('user',)

        widgets = {
            "image": forms.TextInput(attrs={
                "placeholder": "URL field: http//..."
            }),
            "price_per_night": forms.TextInput(attrs={
                "placeholder": "Price in Euro"
            }),
        }
