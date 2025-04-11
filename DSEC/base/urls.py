# base/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from . import views
from .views import my_projects_view, add_MyProjectsView, trashed_project_view, update_MyProjectsView ,project_scans_view, get_all_users


urlpatterns = [
    path('projects/', my_projects_view, name='scan-list'),
    path('project/add/', add_MyProjectsView, name='scan-add'),
    path('project/<str:project_id>/trash/',update_MyProjectsView , name='move_to_trash'),
    path('project/<str:project_id>/', project_scans_view, name='project-scans'),
    path('project/trash/', trashed_project_view, name='trashed_scans'),


    path('users/', get_all_users, name='get-all-users'),
]



