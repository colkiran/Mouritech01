from django.shortcuts import render, redirect
from .models import Products
from django.contrib import messages
# Create your views here.

def index(request):
    prod = Products.objects.all()
    context = {
        'prod':prod,
    }
    return render(request, "index.html", context)


def add(request):
    messages.success(request, request.method)
    if request.method == 'POST':
        pname = request.POST.get('prodnm')
        manuf = request.POST.get('mnfc')
        cat = request.POST.get('catg')
        prc = request.POST.get('prc')

        messages.success(request, pname + manuf + cat + prc)

        prod = Products (
            prodname = pname,
            manufacturer = manuf,
            category = cat,
            price = prc
        )
        prod.save()
        return redirect('home')