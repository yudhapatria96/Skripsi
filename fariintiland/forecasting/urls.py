from django.urls import path, include
from . import views

app_name = "forecasting"

urlpatterns = [
    path('', views.index , name='index'),

]