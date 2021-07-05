from django.urls import path
from .views import home,addtask
urlpatterns=[
    path("list/",home,name="task-list"),
    path("add/",addtask,name="task-add")
]