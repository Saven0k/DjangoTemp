from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('ads.urls'), name='home'),
    path('login', views.login, name="login"),
    path('register', views.registration, name="registration"),
    path('logout', views.logout, name="logout"),
    path('ads', include('ads.urls'), name="ads"),
]
