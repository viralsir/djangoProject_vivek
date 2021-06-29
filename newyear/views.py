from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    date=datetime.utcnow().date()
    return render(request,"newyear/home.html",{
        "is_newyear": date.day==1 and date.month==1
    })
