from django.urls import path

from . import views

app_name = 'hitch'

urlpatterns = [
    path('', views.index, name='index'),
    path('mode', views.mode, name='mode'),
    path('rideMode', views.rideMode, name='rideMode'),
    path('rides', views.rides, name='rides'),
    path('oldRides', views.oldRides, name='oldRides'),
    path('driverMode', views.driverMode, name='driverMode'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('rideForm', views.rideForm, name='rideForm'),
    path('oldDrives', views.oldDrives, name='oldDrives'),
]
