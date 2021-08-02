from django.urls import  path
from emp_app.views import employee_list,new_employee,employee_detail
urlpatterns=[
    path("list/",employee_list,name="emp_list"),
    path("new/",new_employee,name="emp-new"),
    path("detail/<int:eid>",employee_detail,name="emp-detail")
]