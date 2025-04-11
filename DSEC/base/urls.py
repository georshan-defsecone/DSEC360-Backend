from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import get_all_users,create_user,get_authenticated_user

urlpatterns = [
    path('users/', get_all_users, name='get-all-users'),
    path('users/createuser',create_user,name='create-user'),
    path('users/userinfo',get_authenticated_user,name='userinfo')
    
]