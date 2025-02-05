import re
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout as user_logout, login as user_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def login(request):
    error = ''
    if request.method == "POST":
        loginU = request.POST.get("login")
        passwordU = request.POST.get("password")
        
        req = authenticate(request, username=loginU, password=passwordU)
        if req is not None:
            user_login(request, req)
            return HttpResponseRedirect('ads/my')
        else:
            error = 'Вы уже в аккаунте'
            return render(request, 'main/login.html' ,{"error":error})
    return render(request, 'main/login.html')
            

def registration(request):
    error = ''
    if request.method == "POST":
        loginU = request.POST.get("login")
        passwordU = request.POST.get("password")
        passwordU2 = request.POST.get("password2")
        if get_user_model().objects.filter(email=loginU).exists():
            error = 'Пользователь с таким email уже зарегестрирован'
            return render(request, 'main/registration.html', {"error": error})
        else:
            if passwordU == passwordU2:
                pattern = r'^(?=.*[А-ЯЁ])(?=.*[а-яё])(?=.*\d).{8,12}$'
                if not re.match(pattern, passwordU):
                    error = "Пароль должен содержать хотя бы одну заглавную и одну строчную русскую букву, а также хотя бы одну цифру. Длина от 8 до 12 символов."
                    return render(request, "main/registration.html",  {'error':error})
                else:
                    User.objects.create_user(username=loginU, email=loginU, password=passwordU)
                    req = authenticate(request, username=loginU, password=passwordU)
                    if req is not None:
                        return HttpResponseRedirect('/login')
            else:
                error = 'Пароли не совпадают'
                return render(request, 'main/registration.html', {"error": error})
            
    return render(request, 'main/registration.html')

def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/')

