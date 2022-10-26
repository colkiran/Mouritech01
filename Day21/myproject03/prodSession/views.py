import re

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "swelcome.html", {'gname': 'Rahul Dravid'})

def setsession(request):
    request.session['prdname'] = 'NIKE'
    request.session['product'] = 'Jersy'
    return render(request, 'setsession.html')

def getsession(request):
    pname = request.session['prdname']
    prd = request.session['product']
    key = request.session.keys()
    item  = request.session.items()
    prc = request.session.setdefault('price', 5300.00)
    return render(request, "getSession.html", {'prdname': pname, 'product': prd, 'keys': key, 'items': item, 'price':prc})

def delsession(request):
    if 'prdname' in request.session:
        request.session.clear()
    return render(request, "delSession.html")