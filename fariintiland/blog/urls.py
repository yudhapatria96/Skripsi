from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('jurnal/', views.jurnal, name='jurnal'),
    path('berita/', views.berita, name='berita'),
    path('<int:angka>/', views.angka),
    path('category/<str:category>/', views.category, name='category'),
    path('post/<slug:slug>/', views.singlePost, name='singlepost'),

    path('', views.index, name= 'index'),
]