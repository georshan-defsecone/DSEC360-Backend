# base/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import get_all_users
from .views import my_projects_view, add_MyProjectsView, trashed_project_view, update_MyProjectsView

urlpatterns = [
    path('projects/', my_projects_view, name='scan-list'),
    path('project/add/', add_MyProjectsView, name='scan-add'),
    path('project/<str:project_id>/trash/', update_MyProjectsView, name='move_to_trash'),
    path('project/trash/', trashed_project_view, name='trashed_scans'),


    path('users/', get_all_users, name='get-all-users'),
]



