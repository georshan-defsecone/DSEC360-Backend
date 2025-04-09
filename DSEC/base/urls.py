from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import get_all_users

urlpatterns = [
    path('users/', get_all_users, name='get-all-users'),
    
]