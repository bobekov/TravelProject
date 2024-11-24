from django.contrib.auth import get_user_model
from django.db import models
from travel_project.flight.models import Flight
from travel_project.hotel.models import Hotel
from travel_project.room.models import Room


UserModel = get_user_model()


class BookingFlight(models.Model):
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE
    )
    booking_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )


class BookingRoom(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE
    )
    booking_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )