from django.urls import path, converters
from . import views

urlpatterns = [
    path('', views.index),
    path('get_guinness_world_records/', views.get_guinness_world_records)
]