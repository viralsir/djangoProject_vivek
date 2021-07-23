from django.shortcuts import render
from .models import flight
# Create your views here.
def home(request):
    no_of_flights=flight.objects.all()
    return render(request,"flights/home.html",{
        "no_of_flights":no_of_flights
    })

def flight_detail(request,fid):
    flight_info=flight.objects.get(id=fid)
    return render(request,"flights/flight_info.html",{
        "flight_info":flight_info
    })