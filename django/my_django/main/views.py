from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import (
    login as user_login,
    authenticate,
    logout as user_logout,
    get_user_model,
)
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, "main/index.html")


def login(request):
    error = ""
    if request.method == "POST":
        loginU = request.POST.get("login")
        passwordU = request.POST.get("password")

        reg = authenticate(request, username=loginU, password=passwordU)
        if reg is not None:
            user_login(request, reg)
            return HttpResponseRedirect("ads")
        else:
            error = "Ошибка входа, проверьте ввдеенные данные "
            return render(request, "main/login.html", {"error": error})

    return render(request, "main/login.html")


def reg(request):
    error = ""
    if request.method == "POST":
        loginU = request.POST.get("login")
        passwordU = request.POST.get("password")
        passwordU2 = request.POST.get("password2")

        if get_user_model().objects.filter(email=loginU).exists():
            error = "Пользователь с таким email уже существует"
            return render(request, "main/reg.html", {"error": error})
        else:
            if passwordU == passwordU2:
                User.objects.create_user(
                    username=loginU, email=loginU, password=passwordU
                )
                reg = authenticate(request, username=loginU, password=passwordU)
                if reg is not None:
                    return HttpResponseRedirect("login")
                else:
                    error = "Ошибка данных, проверьте введенные данные "
                    return render(request, "main/reg.html", {"error": error})

    return render(request, "main/reg.html")


def logout(request):
    user_logout(request)
    return HttpResponseRedirect("ads")
