from django.contrib.auth import get_user_model
from django.db import models
from travel_project.flight.validators import flight_price

UserModel = get_user_model()


class AirlineChoices(models.TextChoices):
        QATAR_AIRWAYS = 'Qatar Airways', 'Qatar Airways'
        RYANAIR = 'Ryanair', 'Ryanair'
        BRITISH_AIRWAYS = 'British Airways', 'British Airways'
        EMIRATES = 'Emirates', 'Emirates'
        SINGAPORE_AIRLINES = 'Singapore Airlines', 'Singapore Airlines'
        LUFTHANSA = 'Lufthansa', 'Lufthansa'


class Flight(models.Model):
    flight_number = models.CharField(
        max_length=10,
        unique=True)
    destinations = models.CharField(max_length=40)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[
            flight_price
        ]
    )
    airlines = models.CharField(
        max_length=30,
        choices=AirlineChoices.choices
    )
    airlines_logo = models.URLField()
    is_direct = models.BooleanField()

    def flight_duration(self):
        return self.arrival_time - self.departure_time

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
