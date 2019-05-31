from django.db import models

# Create your models here.

class PostModel(models.Model):
    id_penjualan = models.AutoField(primary_key = True)
    bulan_transaksi =  models.CharField(max_length= 255,  null = False, unique= True)
    tahun_transaksi = models.CharField(max_length= 255,  null = False, unique= True)
    jumlah_hotel = models.IntegerField( null = False)
    jumlah_mall = models.IntegerField( null = False)
    jumlah_apartemen = models.IntegerField(   null= False)
    jumlah_C441 = models.IntegerField(   null= False)
    jumlah_C442 = models.IntegerField(   null= False)
    jumlah_C443 = models.IntegerField(   null= False)
    jumlah_C451 = models.IntegerField(   null= False)
    jumlah_C452 = models.IntegerField(   null= False)
    jumlah_C453 = models.IntegerField(   null= False)
    jumlah_C461 = models.IntegerField(   null= False)
    jumlah_C462 = models.IntegerField(   null= False)
    jumlah_C463 = models.IntegerField(   null= False)
    jasa_pembersih_air= models.IntegerField(   null= False)
    jasa_pembersih_kerak_sillica = models.IntegerField(   null= False)
    jasa_pembersih_cooling_tower = models.IntegerField(   null= False)
    jasa_pembersih_stp = models.IntegerField(   null= False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.tahun_transaksi,  self.id_penjualan)