from django.shortcuts import render


# Create your views here.
def index(req):
    return render(req, 'index.html')


def dashboard(req):
    return render(req, 'dashboard.html')
