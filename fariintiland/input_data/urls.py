from django.urls import path

from . import views

app_name = "input_data"

urlpatterns = [
    path('', views.index , name='index'),
    path('input/', views.create , name='input'),
]
