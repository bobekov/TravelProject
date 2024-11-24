from django.contrib.auth import get_user_model
from django.db import models
from travel_project.user_profile.validators import validate_phone_number

UserModel = get_user_model()


class PaymentChoices(models.TextChoices):
    CREDIT_CARD = 'Credit card', 'Credit card'
    PAYPAL = 'Paypal', 'Paypal'
    BANK_TRANSFER = 'Bank transfer', 'Bank transfer'
    CRYPTO = 'Crypto', 'Crypto'


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    star_rating = models.IntegerField(
        choices=[
            (i, i) for i in range(1, 6)
        ],
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[
            validate_phone_number
        ]
    )
    address = models.CharField(max_length=100)
    amenities = models.TextField()
    check_in_time = models.TimeField()
    available_rooms = models.PositiveIntegerField(default=0)
    payment_method = models.CharField(
        max_length=30,
        choices=PaymentChoices.choices,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    @property
    def stars_display(self):
        return "★" * self.star_rating
