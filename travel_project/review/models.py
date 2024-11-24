from django.contrib.auth import get_user_model
from django.db import models

from travel_project.destination.models import Destination
from travel_project.user_profile.models import UserProfile


UserModel = get_user_model()


class Review(models.Model):
    profile = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
    )
    destination = models.ForeignKey(
        to=Destination,
        on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(
        choices=[
            (i, i) for i in range(1, 11)
        ],
    )
    comment = models.TextField(
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(
        default=False
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        if self.destination:
            return self.destination.name if self.destination.name else "Unnamed Destination"
        return "Unknown Destination"

    @property
    def stars_display(self):
        return "★" * self.rating

