from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('scans/', views.MyProjectsView.as_view(), name='scan-list'),
    path('scans/add/', views.add_MyProjectsView, name='scan-add'),
    path('scans/<str:scan_id>/trash/', views.update_MyProjectsView, name='move_to_trash'),
    path('scans/trashed/', views.trashed_scans_view, name='trashed_scans'),
    path('scans/compliance/configaudit/<str:os_name>/', views.get_compliance_data, name='compliance-data'),
    path('scans/compliance/ioc/<str:os_name>/', views.get_compromise_assessment_data, name='compromise-assessment-data'),
   

]



