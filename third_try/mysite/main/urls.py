from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('ads', include('ads.urls'), name="ads"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"), 
]
