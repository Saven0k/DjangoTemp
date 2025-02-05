from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('ads.urls'), name="home" ),
    path('ads', include('ads.urls')),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
]
