from django.urls import path, include
from .views import index

app_name = "komparasi"

urlpatterns = [
    path('', index , name='index'),
  
]