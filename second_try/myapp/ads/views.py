

from django.shortcuts import render
from flask import redirect
from .models import Ad
from django.core.serializers import serialize
from .forms import AdForm
from django.db.models.query import Q
from django.views.generic import UpdateView, DetailView
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.

class AdDetails(DetailView):
    model = Ad
    template_name = 'ads/ad.html'
    context_object_name = 'ad'
class UpdateAd(UpdateView):
    model = Ad
    template_name = 'ads/update.html'
    fields = ['status']
    
def create(request):
    error = ''
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AdForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/ads')
            else:
                error = 'Ошибка'

        form = AdForm
        data = {
            "error": error,
            "form": form,
        }
        return render(request, 'ads/create.html', data)
    else:
        return render(request, 'ads/create.html')

def ads(request):
    ads = Ad.objects.all()
    if request.method == "GET" and 'query' in request.GET:
        query = request.GET.get('query')
        query_text = Q(title__icontains=query) or Q(discription__icontains=query)
        ads = Ad.objects.filter(query_text)
    return render(request, 'ads/ads.html', {"ads": ads})

def my(request):
    if request.user.is_authenticated: 
        ads = [el for el in Ad.objects.all() if el.email == request.user.email]
        return render(request, 'ads/my.html', {"ads":ads})
    else:
        return redirect('/ads')
    
def json(request):
    if request.user.is_superuser:
        queryset = Ad.objects.all()
        data = serialize('json', queryset)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponseRedirect('/')