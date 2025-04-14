# base/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views



urlpatterns = [
   # Projects
    path('projects/', views.get_projects_view),
    path('project/create/', views.create_project_view),
    path('project/trash/<str:project_id>/', views.update_project_view),
    path('projects/trash/', views.trashed_projects_view, name='trashed-projects'),


    # Scans
    path('scans/', views.get_scans_view),
    path('scans/create/', views.create_scan_view),
    path('scans/update/<int:pk>/', views.update_scan_view),


    path('scans/project/<str:project_id>/', views.get_project_scans_view),

]



