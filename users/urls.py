from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'sign-in'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'sign-out'),
    path('register/', RegisterUser.as_view(), name = 'sign-up'),
    path('profile/', ProfileAPIView.as_view(), name = 'profile'),
]