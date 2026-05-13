from django.db import models
from odtman.model_base import TimeStampedModel

# Create your models here.
class Client(TimeStampedModel):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.full_name}'