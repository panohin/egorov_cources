from django.urls import path, converters
from . import views

urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('type/', views.list_of_types),
    path('type/<zodiac_type>/', views.sighs_by_type, name='zodiac_type_url'),
    path('<int:zodiac_sign>/', views.info_about_zodiac_sign_by_number),
    path('<str:zodiac_sign>/', views.info_about_zodiac_sign, name='horoscope_URL')
]