from django.core.exceptions import ValidationError


def flight_price(value):
    if value <= 0:
        raise ValidationError("The price cannot be less than or equal to 0!")