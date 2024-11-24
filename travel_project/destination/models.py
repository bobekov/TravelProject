from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Destination(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True)
    description = models.TextField()
    country = models.CharField(max_length=40)
    city = models.CharField(
        max_length=100,
        blank=True)
    attractions = models.TextField()
    image = models.URLField()
    best_time_to_visit = models.CharField(
        max_length=100,
        blank=True)

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name if self.name else "Unnamed Destination"


