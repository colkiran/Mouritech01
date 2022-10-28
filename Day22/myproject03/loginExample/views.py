from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "loginhome.html", {'gstname': 'Mike Tyson'})

def login(request):
    return render(request, "login.html")

def setssntime(request):
    if request.method == 'POST':
        usrName = request.POST['nm']
        request.session['usrname'] = usrName
        request.session.set_expiry(0)
        return render(request, "loginssntime.html")
    else:
        if 'usrname' in request.session:
            return render(request, "loginssntime.html")
        return render(request, "login.html")