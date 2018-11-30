from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Apartment(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.TextField()
    street = models.TextField()
    deleted = models.BooleanField()
    shower = models.BooleanField()
    bathtub = models.BooleanField()
    microwave = models.BooleanField()
    balcony = models.BooleanField()
    water_included = models.BooleanField()
    heating_included = models.BooleanField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.city