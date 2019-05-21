from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news),
    path('cerita/', views.cerita),
    path('', views.index),
]