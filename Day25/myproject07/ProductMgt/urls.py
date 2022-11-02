
from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_show, name="add"),
    path("updatedata/<int:id>", views.updatedata, name="updatedata"),
    path("deletdata/<int:id>", views.deletedata, name="deletedata")
]