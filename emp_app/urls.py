from django.urls import  path
from emp_app.views import employee_list
urlpatterns=[
    path("list/",employee_list,name="emp_list")
]