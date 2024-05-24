from django.db import models
from django.contrib.auth.models import User as auth_user
# Create your models here.



class Ticket(models.Model):
    user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE, default=1)
    departure = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    departure_airport_code = models.CharField(max_length=10)
    destination = models.CharField(max_length=100)
    destination_airport = models.CharField(max_length=100)
    destination_airport_code = models.CharField(max_length=10)
    departure_date = models.DateField()
    destination_date = models.DateField()
    departure_time = models.TimeField()
    destination_time = models.TimeField()
    duration = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    flightClass = models.CharField(max_length=100)
    price = models.IntegerField()


class Flights(models.Model):
    departure = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    departure_airport_code = models.CharField(max_length=10)
    destination = models.CharField(max_length=100)
    destination_airport = models.CharField(max_length=100)
    destination_airport_code = models.CharField(max_length=10)
    departure_date = models.DateField()
    destination_date = models.DateField()
    departure_time = models.TimeField()
    destination_time = models.TimeField()
    duration = models.CharField(max_length=100)
    airline = models.CharField(max_length=100)
    flightClass = models.CharField(max_length=100)
    price = models.IntegerField()