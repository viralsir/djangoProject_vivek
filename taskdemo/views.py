from django.shortcuts import render

# Create your views here.
tasks=["check balance","recharge mobile",'visit showroom']

def home(request):
    return render(request,"taskdemo/home.html",{
        "tasklist":tasks
    })

def addtask(request):
    return render(request,"taskdemo/addtask.html")