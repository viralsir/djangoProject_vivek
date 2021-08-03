from django.urls import  path
from emp_app.views import employee_list,new_employee,employee_detail,update_employee,delete_employee
urlpatterns=[
    path("list/",employee_list,name="emp_list"),
    path("new/",new_employee,name="emp-new"),
    path("detail/<int:eid>",employee_detail,name="emp-detail"),
    path("update/<int:eid>",update_employee,name="emp-update"),
    path("delete/<int:eid>",delete_employee,name="emp-delete")
]