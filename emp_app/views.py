from django.shortcuts import render
from emp_app.models import employee
# Create your views here.
def employee_list(request):
    emplist=employee.objects.all()

    return render(request,"emp_app/list.html",{
        "employee_list":emplist

    })