
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("setcookie/", views.setcookie, name="setcookie"),
    path("getcookie/", views.getcookie, name="getcookie"),
    path("deletecookie/", views.deletecookie, name="delcookie"),
]