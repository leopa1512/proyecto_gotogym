from django.urls import path
from django.contrib.auth import views as auth_views  ##Vistas para el login
from applogin.views import *

app_name = "config"

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='apploginp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='apploginp/login.html'), name='logout'),
]