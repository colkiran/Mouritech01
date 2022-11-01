from django.shortcuts import render,HttpResponseRedirect
from .models import Product
from .forms import ProductDetails

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = ProductDetails(request.POST)
        if fm.is_valid():
            pid = fm.cleaned_data['Prodid']
            pnm = fm.cleaned_data['Prodname']
            cat = fm.cleaned_data['Category']
            pt = fm.cleaned_data['Prodtype']
            prc = fm.cleaned_data['Price']
            reg = Product(Prodid = pid, Prodname=pnm, Category=cat, Prodtype=pt, Price=prc)
            reg.save()
            fm = ProductDetails()
    else:
        fm=ProductDetails()
    stud = Product.objects.all()
    return render(request, 'add.html', {'form':fm, 'stu':stud})

def updatedata(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        fm = ProductDetails(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        pi = Product.objects.get(pk=id)
        fm = ProductDetails(instance=pi)
    return render(request, 'update.html', {'form': fm})


def deletedata(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
