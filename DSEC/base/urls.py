# base/urls.py
from django.urls import path
from .views import MyProjectsView, add_MyProjectsView, update_MyProjectsView

urlpatterns = [
    path('api/scans/', MyProjectsView.as_view(), name='scan-list'),
    path('api/scans/add/', add_MyProjectsView, name='scan-add'),
    path('api/scans/<str:scan_id>/trash/', update_MyProjectsView, name='move_to_trash'),

]
