from django.urls import  path
from .views import home,about,greetings
urlpatterns=[
    path("main_page/",home,name="hello-home"),
    path("about/",about,name="hello-about"),
    path("greetings/<str:name>",greetings,name="greetings")
]