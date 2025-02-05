from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from .models import Ad
from .forms import AdForm
from django.db.models.query import Q

# Create your views here.


def ads(request):
    ads = [ad for ad in Ad.objects.all() if ad.status]
    if request.method == "GET" and request.GET.get("querry"):
        querry = request.GET.get("querry")
        querry_text = Q(title__icontains=querry) or Q(disc__icontains=querry)
        ads = Ad.objects.filter(querry_text) 
    return render(request, 'ads/ads.html', {"ads":ads})
    

def my(request):
    if request.user.is_authenticated: 
        print(request.user.email)
        ads = [ad for ad in Ad.objects.all() if ad.email == request.user.email]
        return render(request, 'ads/my.html', {"ads":ads})
    else:
        return HttpResponseRedirect('/')

def create(request):
    print(request.user)
    if request.user.is_authenticated:   
        error = ''
        if request.method == "POST":
            form = AdForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                error = 'Ошибка данных'
        form = AdForm
        data = {
            "error": error,
            "form": form
        }
        return render(request, 'ads/create.html', data)
    else:
        return HttpResponseRedirect('/')

def json(request):
    if request.user.is_superuser:    
        ads = Ad.objects.all()
        return render(request, 'ads/json.html', {"ads":ads})
    else:
        return HttpResponseRedirect('/')

class AdUpdate(UpdateView):
    model = Ad
    template_name = 'ads/update.html'
    fields = ["status"]
    
class AdDetails(DetailView):
    model = Ad
    template_name = 'ads/ad.html'
    context_object_name = 'ad'
    