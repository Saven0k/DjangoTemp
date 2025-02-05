from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ads, name='ads'),
    path('create', views.create, name='create'),
    path('/<int:pk>/update', views.UpdateAd.as_view(), name='update'),
    path('/create', views.create, name='create'),
    path('/<int:pk>', views.AdDetails.as_view(), name='ad'),
    path('/ads.json', views.json, name='json'),
    path('/my', views.my, name="my"),
]
