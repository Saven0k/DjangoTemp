from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ads', include('ads.urls'), name="ads"),
    path('login', views.login, name="login"),
    path('reg', views.reg, name="reg"),
    path('logout', views.logout, name="logout"),
]
