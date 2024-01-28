from django.shortcuts import render

from .models import userinfo


# Create your views here.
def HOME(request):
    return render(request, template_name=r'HTML/HOME.html')


def login(request):
    return render(request, template_name=r'HTML/login.html')


def Register(request):
    return render(request, template_name=r'HTML/Register.html')

def Userinfo(request):
    info = userinfo.objects.all()
    inf = {"details": info}
    return render(request,template_name=r"database/userinfo.html",context=inf)
