from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request,"hello/home.html")

def about(request):
    return render(request,"hello/about.html")

def greetings(request,name):
    return HttpResponse("<h1> Hello "+name+"</h1>")