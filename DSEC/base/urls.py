# base/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import get_all_users
from .views import MyProjectsView, add_MyProjectsView, trashed_scans_view, update_MyProjectsView, compliance_data

urlpatterns = [
    path('scans/', MyProjectsView.as_view(), name='scan-list'),
    path('scans/add/', add_MyProjectsView, name='scan-add'),
    path('scans/<str:scan_id>/trash/', update_MyProjectsView, name='move_to_trash'),
    path('scans/trashed/', trashed_scans_view, name='trashed_scans'),
    path('users/', get_all_users, name='get-all-users'),
    path('compliance/<str:os_name>/', compliance_data, name='compliance-data'),

]



