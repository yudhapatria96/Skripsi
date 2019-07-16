from django.urls import path, include
from .views import index, hasilKomparasi, hasilKomparasiTahun, indextahun, hasilKomparasiItem, hasilKomparasiTahunIndex

app_name = "komparasi"

urlpatterns = [
    path('', index , name='index'),
    path('indextahun/', indextahun , name='indextahun'),

    path('hasilkomparasi/', hasilKomparasi, name ='hasilkomparasi' ),
    path('hasilkomparasiitem/', hasilKomparasiItem, name ='hasilkomparasiitem' ),

    path('hasilkomparasitahun/', hasilKomparasiTahun, name ='hasilkomparasitahun' ),
    path('hasilkomparasitahunitem/', hasilKomparasiTahunIndex, name ='hasilkomparasitahunitem' ),


]