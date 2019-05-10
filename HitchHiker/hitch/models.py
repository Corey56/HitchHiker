import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class Cadet(models.Model):
    xnum = models.CharField(max_length=6)
    phoneNum = models.IntegerField()
    classYear = models.IntegerField()
    def __str__(self):
        return self.xnum

class Vehicle(models.Model):
    driver = models.ForeignKey(Cadet, on_delete=models.CASCADE)
    carMake = models.CharField(max_length=20)
    carModel = models.CharField(max_length=30)
    carColor = models.CharField(max_length=20)
    def __str__(self):
        return '%s %s %s' % (self.carMake, self.carModel, self.carColor)

class Destination(models.Model):
    destination = models.CharField(max_length=50)
    def __str__(self):
        return self.destination

class Ride(models.Model):
    destination = models.ManyToManyField(Destination)
    passengers = models.ManyToManyField(Cadet)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    departureTime = models.DateTimeField()
    seatsAvailable = models.IntegerField()
    storageAvailable = models.CharField(max_length=30)
    departureLocation = models.CharField(max_length=30)
    comments = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return '%s %s' % (self.vehicle.driver, self.departureTime)
