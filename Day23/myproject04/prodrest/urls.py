
from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view()),
    path("productOne/<str:pid>", views.ProductList.as_view())
]