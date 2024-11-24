from django import forms

from travel_project.hotel.models import Hotel


class AddHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        exclude = ('user',)

        widgets = {
            "check_in_time": forms.TimeInput(attrs={
                'type': "time"
            }),
            "amenities": forms.Textarea(attrs={
                "placeholder": "e.g. parking, free Wi-Fi, pool, gym, spa, airport transfer, room service"
            }),
        }
