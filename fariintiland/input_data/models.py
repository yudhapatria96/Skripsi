from django.db import models

# Create your models here.
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)  

def validate_even(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

class PenjualanModel(models.Model):
    
    MONTH_CHOICES = (
    ('januari','Januari'),
    ('februari', 'Februari'),
    ('maret','Maret'),
    ('april','April'),
    ('mei','Mei'),
    ('juni', 'Juni'),
    ('juli', 'Juli'),
    ('agustus', 'Agustus'),
    ('september', 'September'),
    ('oktober', 'Oktober'),
    ('november', 'November'),
    ('desember', 'Desember')
    )
    id_penjualan                    = models.AutoField(primary_key = True)
    bulan_transaksi                 =  models.CharField(max_length= 200, choices=MONTH_CHOICES, default='Januari')
    tahun_transaksi                 = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(2009), max_value_current_year])
    jumlah_hotel                    = models.IntegerField(   null = False, default= 0, validators=[validate_even])
    jumlah_mall                     = models.IntegerField(   null = False, default= 0, validators=[validate_even])
    jumlah_apartemen                = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C441                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C442                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C443                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C451                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C452                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C453                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C461                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C462                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_C463                     = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jasa_pembersih_air              = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jasa_pembersih_kerak_sillica    = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jasa_pembersih_cooling_tower    = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jasa_pembersih_stp              = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_asam_sulfat              = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_molases                  = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_hcl                      = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    jumlah_abf                      = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    pendapatan                      = models.IntegerField(   null= False, default= 0, validators=[validate_even])
    create_time                     = models.DateTimeField(auto_now_add=True)
    update_time                     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.tahun_transaksi,  self.id_penjualan)
    