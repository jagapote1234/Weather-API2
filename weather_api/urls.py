from django.urls import path
from . import views

app_name = 'weather_api'

urlpatterns = [
    path('', views.IndexView, name='index'),
]