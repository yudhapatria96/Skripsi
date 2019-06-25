from django.db import models

# Create your models here.

class PenjualanModel(models.Model):
    id_penjualan                    = models.AutoField(primary_key = True)
    bulan_transaksi                 =  models.CharField(max_length= 200,  null = False, unique= False)
    tahun_transaksi                 = models.IntegerField(null = False, default = 2010)
    jumlah_hotel                    = models.IntegerField(   null = False, default= 0)
    jumlah_mall                     = models.IntegerField(   null = False, default= 0)
    jumlah_apartemen                = models.IntegerField(   null= False, default= 0)
    jumlah_C441                     = models.IntegerField(   null= False, default= 0)
    jumlah_C442                     = models.IntegerField(   null= False, default= 0)
    jumlah_C443                     = models.IntegerField(   null= False, default= 0)
    jumlah_C451                     = models.IntegerField(   null= False, default= 0)
    jumlah_C452                     = models.IntegerField(   null= False, default= 0)
    jumlah_C453                     = models.IntegerField(   null= False, default= 0)
    jumlah_C461                     = models.IntegerField(   null= False, default= 0)
    jumlah_C462                     = models.IntegerField(   null= False, default= 0)
    jumlah_C463                     = models.IntegerField(   null= False, default= 0)
    jasa_pembersih_air              = models.IntegerField(   null= False, default= 0)
    jasa_pembersih_kerak_sillica    = models.IntegerField(   null= False, default= 0)
    jasa_pembersih_cooling_tower    = models.IntegerField(   null= False, default= 0)
    jasa_pembersih_stp              = models.IntegerField(   null= False, default= 0)
    jumlah_asam_sulfat              = models.IntegerField(   null= False, default= 0)
    jumlah_molases                  = models.IntegerField(   null= False, default= 0)
    jumlah_hcl                      = models.IntegerField(   null= False, default= 0)
    jumlah_abf                      = models.IntegerField(   null= False, default= 0)
    pendapatan                      = models.IntegerField(   null= False, default= 0)
    create_time                     = models.DateTimeField(auto_now_add=True)
    update_time                     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.tahun_transaksi,  self.id_penjualan)