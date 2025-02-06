from django.shortcuts import redirect, render
from .models import Ad
from .forms import AdForm

from django.db.models.query import Q
from django.views.generic import UpdateView, DetailView
# Create your views here.
def my(request):
    if request.user.is_authenticated:
        ads = [ad for ad in Ad.objects.all() if ad.status and ad.email == request.user.email]
        return render(request, 'ads/my.html', {"ads":ads})
    else:
        return redirect('/')

def ads(request):
    ads = [ad for ad in Ad.objects.all() if ad.status]
    if request.method == "GET" and "querry" in request.GET:
        querry = request.GET.get("querry")
        querry_text = Q(title__icontains=querry) or Q(disc__icontains=querry)
        ads = ads.filter(querry_text)
    return render(request, 'ads/ads.html', {"ads":ads})

def new(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == "POST":
            form = AdForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                error = 'Ошибка, проверьте введенные данные'
                return render(request, 'ads/new.html', {"error":error})
        
        form = AdForm
        data =  {
            "form": AdForm,
            "error":error, 
        }
        
        return render(request, 'ads/new.html', data)
    else:
        return redirect('/')


class AdDetails(DetailView):
    model = Ad
    template_name = 'ads/ad.html'
    context_object_name = 'ad'


class AdUpdate(UpdateView):
    model= Ad
    template_name = "ads/update.html"
    fields = ['status']


def json(request):
    if request.user.is_superuser:
        ads = Ad.objects.all()
        return render(request, 'ads/json.html', {"ads":ads})
    else:
        return redirect('/')