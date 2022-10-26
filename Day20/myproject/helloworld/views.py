from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(requests):
    return HttpResponse("<h1> Hello World </h1>")