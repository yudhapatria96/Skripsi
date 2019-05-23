from django.urls import path
from . import views

urlpatterns = [
    path('jurnal/', views.jurnal),
    path('berita/', views.berita),
    path('<int:angka>/', views.angka),
    path('', views.index),
]