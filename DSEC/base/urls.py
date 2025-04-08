# base/urls.py
from django.urls import path
from .views import MyProjectsView, add_MyProjectsView

urlpatterns = [
    path('api/scans/', MyProjectsView.as_view(), name='scan-list'),
    path('api/scans/add/', add_MyProjectsView, name='scan-add'),
]
