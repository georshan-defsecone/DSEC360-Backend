# base/urls.py
from django.urls import path
from .views import MyProjectsView

urlpatterns = [
    path('api/scans/', MyProjectsView.as_view(), name='scan-list'),
]
