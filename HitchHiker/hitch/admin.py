from django.contrib import admin

from .models import Cadet, Vehicle, Destination, Ride

admin.site.register(Cadet)

admin.site.register(Vehicle)

admin.site.register(Destination)

admin.site.register(Ride)
