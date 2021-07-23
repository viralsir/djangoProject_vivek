from django.urls import  path
from . import views
urlpatterns=[
        path("home/",views.home,name="flight-home"),
        path("detail/<int:fid>",views.flight_detail,name="flight-detail")
]