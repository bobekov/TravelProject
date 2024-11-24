from django.contrib.auth import get_user_model
from django.db import models
from travel_project.hotel.models import Hotel


UserModel = get_user_model()


class RoomChoices(models.TextChoices):
    SINGLE = 'Single', 'Single'
    DOUBLE = 'Double', 'Double'
    SUITE = 'Suite', 'Suite'
    FAMILY = 'Family', 'Family'
    DELUXE = 'Deluxe', 'Deluxe'
    STUDIO = 'Studio', 'Studio'


class Room(models.Model):
    hotel = models.ForeignKey(
        to=Hotel,
        on_delete=models.CASCADE
    )
    image = models.URLField()
    room_type = models.CharField(
        max_length=40,
        choices=RoomChoices.choices
    )
    room_number = models.CharField(max_length=500)
    price_per_night = models.DecimalField(
        max_digits=1000,
        decimal_places=2
    )
    description = models.TextField(null=True, blank=True)
    air_conditioning = models.BooleanField(default=False)
    bathtub = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

