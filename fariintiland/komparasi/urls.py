from django.urls import path, include
from .views import index, hasilKomparasi, hasilKomparasiTahun, indextahun

app_name = "komparasi"

urlpatterns = [
    path('', index , name='index'),
    path('indextahun/', indextahun , name='indextahun'),

   path('hasilkomparasi/', hasilKomparasi, name ='hasilkomparasi' ),
      path('hasilkomparasitahun/', hasilKomparasiTahun, name ='hasilkomparasitahun' ),

]