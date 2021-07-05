from django.urls import path
from .views import home,addtask
urlpatterns=[
    path("list/",home,name="task-list"),
    path("create/",addtask,name="task-add")
]