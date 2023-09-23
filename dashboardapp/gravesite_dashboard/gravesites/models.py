from django.db import models

# Create your models here.

class Gravesite(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # Add other fields as needed
