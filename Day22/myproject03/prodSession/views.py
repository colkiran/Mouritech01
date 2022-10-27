import re
import datetime
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

def setssntime(request):
    request.session['prdname'] = 'Reebok'
    request.session.set_expire_at_browser_close = False
    request.session.set_expiry(datetime.timedelta(seconds=30))
    return render(request, "setssntime.html")

def getssntime(request):
    pname = request.session['prdname']
    return render(request, 'getssntime.html', {'prdname': pname})

def delssntime(request):
    request.session.flush()
    return render(request, 'delssntime.html')
