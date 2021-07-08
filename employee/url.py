from django.urls import path
from .views import home,addtask
urlpatterns=[
    path("mainlist/",home,name="employee-list"),
    path("task/",addtask,name="new-task")


]