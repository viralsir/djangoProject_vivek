from django.shortcuts import render
from .models import flight
# Create your views here.
def home(request):
    no_of_flights=flight.objects.all()
    return render(request,"flights/home.html",{
        "no_of_flights":no_of_flights
    })
