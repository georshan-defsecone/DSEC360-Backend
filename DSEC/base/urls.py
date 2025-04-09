from django.urls import path
from .views import add_user
urlpatterns = [
    path('api/users/',add_user, name='insert-data'),
]