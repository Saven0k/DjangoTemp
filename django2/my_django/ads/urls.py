from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ads, name="ads"),
    path('/new', views.new, name="new"),
    path('/<int:pk>', views.AdDetail.as_view(), name="ad"),
    path('/<int:pk>/update', views.AdUpdate.as_view(), name="update"),
    path('/ads.json', views.json, name="json"),
    path('/my', views.my, name="my"),
]