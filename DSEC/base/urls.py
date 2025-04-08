# base/urls.py
from django.urls import path
from .views import MyProjectsView, add_MyProjectsView, trashed_scans_view, update_MyProjectsView

urlpatterns = [
    path('api/scans/', MyProjectsView.as_view(), name='scan-list'),
    path('api/scans/add/', add_MyProjectsView, name='scan-add'),
    path('api/scans/<str:scan_id>/trash/', update_MyProjectsView, name='move_to_trash'),
    path('api/scans/trashed/', trashed_scans_view, name='trashed_scans')

]
