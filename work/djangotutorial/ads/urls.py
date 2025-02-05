from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ads, name='ads' ),
    path('/new', views.create, name="create_ad"),
    path('/<int:pk>', views.AdsDetails.as_view(), name="ad"),
    path('/<int:pk>/update', views.AdsUpdate.as_view(), name="ad_update"),
    path('/ads.json', views.jsonView, name='json'),
    path('/my', views.my, name='my'),
]
