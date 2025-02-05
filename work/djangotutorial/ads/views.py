from django.shortcuts import render, redirect
from .models import Ad
from .forms import AdsForms
from django.db.models import Q
from django.views.generic import DetailView, UpdateView

# Create your views here.
from .models import Ad


def ads(request):
    ads = Ad.objects.all()
    if request.method == "GET" and "query" in request.GET:
        query = request.GET.get("query")
        query_text = Q(title__icontains=query) or Q(discription__icontains=query)
        ads = Ad.objects.filter(query_text)
        context = {"ads": ads}
        return render(request, "ads/ads.html", context)
    else:
        return render(request, "ads/ads.html", {"ads": ads})



class AdsDetails(DetailView):
    model = Ad
    template_name = "ads/ad.html"
    context_object_name = "ad"


class AdsUpdate(UpdateView):
    model = Ad
    template_name = "ads/update.html"
    fields = ["status"]


def create(request):
    error = ""
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AdsForms(request.POST)
            if form.is_valid():
                form.save()
                return redirect("ads")
            else:
                error = "Данные не верные"

        form = AdsForms
        data = {
            "form": form,
            "error": error,
        }
        return render(request, "ads/create.html", data)
    else:
        return redirect("/ads")

def my(request):
    ads = [el for el in Ad.objects.all() if el.email == request.user.email]

    if request.user.is_authenticated:
        return render(request, "ads/my.html", {"ads": ads})
    else:
        return redirect("/ads")


def jsonView(request):
    if request.user.is_superuser:
        data = Ad.objects.all()
        return render(request, "main/json.html", {"data": data})
    else:
        return redirect("/ads")
