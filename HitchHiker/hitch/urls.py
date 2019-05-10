from django.urls import path

from . import views

app_name = 'hitch'

urlpatterns = [
    path('', views.index, name='index'),
    path('mode', views.mode, name='mode'),
    path('<int:cadet>/rideMode', views.rideMode, name='rideMode'),
    path('<int:cadet>/rides', views.rides, name='rides'),
    path('<int:cadet>/oldRides', views.oldRides, name='oldRides'),
    path('<int:cadet>/driverMode', views.driverMode, name='driverMode'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('rideForm', views.rideForm, name='rideForm'),
    path('<int:cadet>/oldDrives', views.oldDrives, name='oldDrives'),
]
