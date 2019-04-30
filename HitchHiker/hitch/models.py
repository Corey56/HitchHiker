import datetime
from django.db import models
from django.utils import timezone


class Cadet(models.Model):
    xnum = models.IntegerField(unique=True)
    phoneNum = models.IntegerField()
    classYear = models.IntegerField()


class Vehicle(models.Model):
    xnum = models.ForeignKey(Cadet, on_delete=models.CASCADE)
    carMake = models.CharField(max_length=20)
    carModel = models.CharField(max_length=30)
    carColor = models.CharField(max_length=20)

class Ride(models.Model):
    driver = models.ForeignKey(Cadet, on_delete=models.CASCADE)
    passengers = models.ManyToManyField(Cadet, verbose_name="Passengers")
    departureTime = models.DateTimeField()
    seatsAvailable = models.IntegerField()
    storageAvailable = models.CharField(max_length=30)
    departureLocation = models.CharField(max_length=30)
    comments = models.CharField(max_length=100, null=True, blank=True)

class Destination(models.Model):
    destination = models.OneToOneField(Ride, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)

class Managers(models.Model):
    lastName = models.CharField(max_length=20)
    firstName = models.CharField(max_length=20)
