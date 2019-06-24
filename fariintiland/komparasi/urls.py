from django.urls import path, include
from .views import index, hasilKomparasi

app_name = "komparasi"

urlpatterns = [
    path('', index , name='index'),
   path('hasilkomparasi/', hasilKomparasi, name ='hasilkomparasi' ),
]