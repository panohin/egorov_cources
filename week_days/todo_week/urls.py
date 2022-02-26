from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("<int:name_of_day>/", views.get_todo_list_on_day_by_number),
    path("<name_of_day>/", views.get_todo_list_on_day, name="name_of_day_url")
    ]