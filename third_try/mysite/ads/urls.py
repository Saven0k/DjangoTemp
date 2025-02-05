from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.ads, name="ads"),
    path('/create', views.create, name="createAds"),
    path('/<int:pk>/update', views.AdUpdate.as_view(), name="update"),
    path('/<int:pk>', views.AdDetails.as_view(), name="ad"), 
    path('/ads.json', views.json, name="json"), 
    path('/my', views.my, name="my"), 
    
]
