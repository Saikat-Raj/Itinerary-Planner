# itineraries/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
