from django.shortcuts import render,redirect
from django import forms

# Create your views here.
tasks=["check balance","recharge mobile",'visit showroom']

def home(request):
    return render(request,"taskdemo/home.html",{
        "tasklist":tasks
    })

class TaskForm(forms.Form):
    task=forms.CharField(max_length=25)
    priority=forms.IntegerField(min_value=1,max_value=7)

def addtask(request):
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            #request.POST["task"]
            tasks.append(form.cleaned_data["task"])
            return redirect('task-list')
        else :
            return render(request, "taskdemo/addtask.html", {
                "form": form
            })
    form=TaskForm()
    return render(request,"taskdemo/addtask.html",{
        "form":form
    })