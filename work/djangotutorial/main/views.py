import re
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import logout as user_logout, login as user_login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



def index(request):
    return render(request, "main/index.html")


def login(request):
    error = ''  
    if request.method == "POST":
        loginU = request.POST.get("login")
        password = request.POST.get("password")
        
        reg = authenticate(request, username=loginU, password=password)
        if reg is not None:
            user_login(request, reg)
            return HttpResponseRedirect('ads')
        else:
            error = 'Ошибка данных'
            return render(request, "main/login.html", {'error':error})
    return render(request, "main/login.html")


def logout(request):
    user_logout(request)
    return HttpResponseRedirect("/")


def register(request):
    error = ''
    if request.method == "POST":
        loginU = request.POST.get("login")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if get_user_model().objects.filter(email=loginU).exists():  
            error = 'Такой email уже зарегестрирован'
            return render(request, "main/register.html", {'error':error})
        else:
            pattern = r'^(?=.*[А-ЯЁ])(?=.*[а-яё])(?=.*\d).{8,12}$'
            
            if not re.match(pattern, password):
                error = "Пароль должен содержать хотя бы одну заглавную и одну строчную русскую букву, а также хотя бы одну цифру. Длина от 8 до 12 символов."
                return render(request, "main/register.html",  {'error':error})
            else:
                if password == password2:
                    User.objects.create_user(username=loginU, email=loginU, password=password)
                    reg = authenticate(request, username=loginU, password=password)
                    if reg is not None:
                        return HttpResponseRedirect('/login')
                    else:
                        error = 'Пароли не совпадают'
                        return render(request, "main/register.html",  {'error':error})
    return render(request, "main/register.html")
