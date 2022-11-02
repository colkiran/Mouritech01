
from django.urls import path
from . import views

urlpatterns = [
    path("employee/", views.EmpList.as_view()),
    path("employee/<int:pk>", views.EmpUpdateDel.as_view())
]