from django.shortcuts import render,redirect
from django import forms

# Create your views here.
tasks=["Employee Name","Employee ID","Employee Dept","Employee Salary"]
data=["Vivek","02","Computer","15000"]
data1=["Vimal","03","IT","15000"]
data2=["Viren","04","backend","25000"]
data3=["Raj","05","database","20000"]
def home(request):
    return render(request,"employee/home.html",{
        "EmployeeList":tasks,
        "data":data,
        "data1":data1,
        "data2":data2,
        "data3":data3
    })

class Taskform(forms.Form):
    task=forms.CharField(max_length=20)

def addtask(request):
    if request.method == 'POST':
        form=Taskform(request.POST)
        if form.is_valid():
            tasks.append((form.cleaned_data["task"]))
            return redirect('Employee-list')
        else:
            return render(request,"employee/task.html",{
                "form": form
            })
    form=Taskform()
    return render(request,"employee/task.html",{
        "form":form
    })