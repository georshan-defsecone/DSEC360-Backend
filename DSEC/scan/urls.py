# base/urls.py
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
   # Projects
    path('projects/', views.get_projects_view),
    path('project/<str:project_id>/', views.get_project_by_id,),
    path('all-projects/', views.get_all_projects_view, name='get_all_projects'),
    path('project/create/', views.create_project_view),
    path('project/trash/<str:project_id>/', views.update_project_view),
    path('projects/trash/', views.trashed_projects_view, ),
    path('project/trash/delete/<str:project_id>/', views.delete_project_view),
    path('projects/trash/deleteAll', views.delete_all_projects_view),


    # Scans
    path('scans/', views.get_scans_view),
    path('scans/create/', views.create_scan_view),
    path('scans/update/<int:pk>/', views.update_scan_view),


    path('scans/project/<str:project_id>/', views.get_project_scans_view),

]



