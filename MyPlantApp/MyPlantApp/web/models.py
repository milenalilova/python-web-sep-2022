from django.db import models
from django.core.validators import MinLengthValidator
from django.core import exceptions


def validate_first_letter_capital(value):
    if not value[0].isupper():
        raise exceptions.ValidationError('Your name must start with a capital letter!')


def validate_only_letters(value):
    if not value.isalpha():
        # if not ch.isalpha:
        raise exceptions.ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(
            MinLengthValidator(2),
        ),

    )

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(validate_first_letter_capital,

                    ),
        verbose_name='First Name'
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            validate_first_letter_capital,
        ),
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    OUTDOOR_PLANTS = "Outdoor Plants"
    INDOOR_PLANTS = "Indoor Plants"

    PLANTS_TYPES = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=14,
        choices=PLANTS_TYPES,
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            MinLengthValidator(2),
            validate_only_letters,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
