from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

CATEGORY = (
    ("Action", "Action"),
    ("Adventure", "Adventure"),
    ("Puzzle", "Puzzle"),
    ("Strategy", "Strategy"),
    ("Sports", "Sports"),
    ("Board/Card Game", "Board/Card Game"),
    ("Other", "Other"),
)


class ProfileModel(models.Model):
    email = models.EmailField(verbose_name="Email")
    age = models.IntegerField(verbose_name="Age", validators=[MinValueValidator(12)])
    password = models.CharField(verbose_name="Password", max_length=30)
    first_name = models.CharField(verbose_name="First Name", max_length=30, null=True, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=30, null=True, blank=True)
    profile_picture = models.URLField(verbose_name="Profile Picture", null=True, blank=True)


class GameModel(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, unique=True)
    category = models.CharField(verbose_name="Category", max_length=30, choices=CATEGORY)
    rating = models.FloatField(verbose_name="Rating", validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])
    max_level = models.IntegerField(verbose_name="Max Level", validators=[MinValueValidator(1)], null=True, blank=True)
    image_url = models.URLField(verbose_name="Image URL")
    summary = models.TextField(verbose_name="Summary", null=True, blank=True)

