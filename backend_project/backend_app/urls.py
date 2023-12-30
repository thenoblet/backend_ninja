
from django.urls import path
from .views import get_basic_info

urlpatterns = [
    path('basic_info/', get_basic_info, name='basic_info')
]