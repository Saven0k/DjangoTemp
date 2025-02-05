from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login as user_login, logout as user_logout, authenticate, get_user_model
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def login(request):
    if request.method == "POST":
        loginU = request.POST.get("login")  
        passwordU = request.POST.get("password")
        reg = authenticate(request, username=loginU, password=passwordU)
        if reg is not None:
            user_login(request,reg)
            return HttpResponseRedirect('ads/my')
        else:
            print(request.user, loginU, passwordU, reg)
            error = 'Вы уже в аккаунте'
            return render(request, 'main/login.html', {"error":error})
    return render(request, 'main/login.html')

    
def register(request):
    error = ''
    if request.method == "POST":
        loginU = request.POST.get("login")
        passwordU = request.POST.get("passoword")
        passwordU2 = request.POST.get("passoword2")
        
        if get_user_model().objects.filter(email=loginU).exists():
            error = 'Пользователя с таким Email уже существует'
            return render(request, 'main/register.html', {"error":error})
            
        else:
            if passwordU == passwordU2:    
                User.objects.create_user(username=loginU,email=loginU, password=passwordU)
                reg = authenticate(request, username=loginU, password=passwordU)
                print(reg,loginU, passwordU,passwordU2 )
                if reg is not None:
                    return HttpResponseRedirect('login')
            else:
                error = 'Пароли не совпадают'
                return render(request, 'main/register.html', {"error":error})
        
      
    return render(request, 'main/register.html')



def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/')