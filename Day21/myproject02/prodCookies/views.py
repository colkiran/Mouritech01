from django.shortcuts import render
import datetime

def home(request):
    return  render(request, "welcome.html", {'gname': 'Sachin Tendulkar'})

# Create your views here.
def setcookie(request):
    response = render(request, "setcookie.html")
    response.set_cookie('prodname', 'adidas', max_age=datetime.timedelta())
    return response

def getcookie(request):
    prdname = request.COOKIES['prodname']
    return render(request, "getcookie.html", {'pname': prdname})


def deletecookie(reqeuest):
    response = render(reqeuest, "deletecookie.html")
    response.delete_cookie('prodname')
    return response
