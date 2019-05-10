from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404
from hitch.forms import cadetForm, vehicleForm, RideForm

from .models import Cadet, Vehicle, Ride, Destination

def index(request):
        if request.method == 'POST':
            form = cadetForm(request.POST)
            if form.is_valid():
                #Add the cadet to the database
                newCadet = form.save()
                cadet = newCadet.id
                context = {'cadet':cadet}
                #Go back to cadet list
                return HttpResponseRedirect('mode', cadet)
        else:
            form = cadetForm()
        return render(request, 'hitch/index.html', {'form': form})

def mode(request, cadet):
    context = {'cadet':cadet}
    return render(request, 'hitch/mode.html', context)

def rideMode(request):
    return render(request, 'hitch/rideMode.html')

def rides(request):
    ride_list = Ride.objects.all()
    context = {'ride_list':ride_list}
    return render(request, 'hitch/rides.html', context)

def oldRides(request, cadet_id):
    cadet = get_object_or_404(Cadet, pk=cadet_id)
    ride_list = Ride.objects.filter(passengers=cadet_id)
    context = {'ride_list':ride_list,'cadet': cadet}
    return render(request, 'hitch/rides.html', context)

def driverMode(request):
    for thing in Cadet.objects.get():
        cadet = thing.xnum
        break
    context = {'cadet':cadet}
    return render(request, 'hitch/driverMode.html', context)

def vehicle(request):
        if request.method == 'POST':
            form = vehicleForm(request.POST)
            if form.is_valid():
                #Add the cadet to the database
                newCar = form.save()
                #Go back to cadet list
                return HttpResponseRedirect('/hitch/rideForm')
        else:
            form = vehicleForm()
        return render(request, 'hitch/vehicle.html', {'form': form})

def rideForm(request):
        if request.method == 'POST':
            form = RideForm(request.POST)
            if form.is_valid():
                #Add the cadet to the database
                newRide = form.save()
                #Go back to cadet list
                return HttpResponseRedirect('/hitch/driverMode')
        else:
            form = RideForm()
        return render(request, 'hitch/rideForm.html', {'form': form})

def oldDrives(request, cadet_id):
    cadet = get_object_or_404(Cadet, pk=cadet_id)
    ride_list = Ride.objects.filter(passengers=cadet_id)
    context = {'ride_list':ride_list,'cadet': cadet}
    return render(request, 'hitch/rides.html', context)
