from django.core import validators, exceptions
from django.core.exceptions import ValidationError
from django.db import models


def validate_min_length(value):
    if len(value) < 2:
        raise exceptions.ValidationError('The username must be a minimum of 2 chars')


def validate_year_in_range(value):
    if not 1980 <= value <= 2049:
        raise ValidationError('Year must be between 1980 and 2049')


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=(
            validate_min_length,
        ),
        null=False,
        blank=False,

    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(18),
        ),
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    SPORTS_CAR = "Sports Car"
    PICKUP_CAR = "Pickup"
    CROSSOVER_CAR = "Crossover"
    MINUBUS_CAR = "Minibus"
    OTHER_CAR = "Other"

    TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP_CAR, PICKUP_CAR),
        (CROSSOVER_CAR, CROSSOVER_CAR),
        (MINUBUS_CAR, MINUBUS_CAR),
        (OTHER_CAR, OTHER_CAR),
    )

    type = models.CharField(
        max_length=10,
        choices=TYPES,
        null=False,
        blank=False,

    )

    model = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(2),
        ),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=(
            validate_year_in_range,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            validators.MinValueValidator(1),
        ),
        null=False,
        blank=False,
    )
