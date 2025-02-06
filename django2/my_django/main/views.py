from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login, logout as user_logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import re


# Create your views here.

def index(request):
    return render(request, 'main/index.html')
def logout(request):
    user_logout(request)
    return redirect('/ads')
def login(request):
    error = ''
    if request.method == "POST":
        loginU = request.POST.get("login")
        passwordU = request.POST.get("password")

        reg = authenticate(request, username=loginU, password=passwordU)
        if reg is not None:
            user_login(request, reg)
            return redirect('ads')
        else:
            error = 'Ошибка данных'
            return render(request, 'main/login.html', {"error":error})
        
        
    return render(request, 'main/login.html')


def reg(request):
    error = ''
    if request.method == "POST":
        loginU = request.POST.get("login")
        passwordU = request.POST.get("password")
        passwordU2 = request.POST.get("password2")
        
        if get_user_model().objects.filter(email=loginU).exists():
            error = 'Пользователь с таким email уже существует'
            return render(request, 'main/reg.html', {"error":error})
        else:
            pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)$'
            if not re.match(pattern, passwordU):
                error = 'Неправильно ввдееные данные'
                return render(request, 'main/reg.html', {"error":error})
            else:
                if passwordU == passwordU2:
                    User.objects.create_user(username=loginU, email=loginU, password=passwordU)
                    reg = authenticate(request, username=loginU, password=passwordU)
                    if reg is not None:
                        return redirect('login')
                    else:
                        error = 'Ошибка данных'
                        return render(request, 'main/reg.html', {"error":error})
                else:
                    error = 'Пароли не равны'
                    return render(request, 'main/reg.html', {"error":error})
    return render(request, 'main/reg.html')