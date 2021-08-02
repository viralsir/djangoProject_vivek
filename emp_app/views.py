from django.shortcuts import render,redirect
from emp_app.models import employee
from .models import employee
# Create your views here.
def employee_list(request):
    emplist=employee.objects.all()

    return render(request,"emp_app/list.html",{
        "employee_list":emplist

    })

def employee_detail(request,eid):
    emp=employee.objects.get(id=eid)
    return render(request,"emp_app/employee_detail.html",{
        "emp":emp
    })


def new_employee(request):
    if request.method == 'POST':
        print(request.POST)
        emp=employee()
        emp.name=request.POST['name']
        emp.address=request.POST['address']
        emp.phno=request.POST['phno']
        emp.salary=request.POST['salary']
        emp.save()
        return redirect('emp_list')
    else:
        return render(request,"emp_app/emp_form.html")