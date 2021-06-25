from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home Page</h1>")
def about(request):
    return HttpResponse("<h1>About Page </h1>")
def greetings(request,name):
    return HttpResponse("<h1> Hello "+name+"</h1>")