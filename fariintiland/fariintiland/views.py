# from django.http import HttpResponse
from django.shortcuts import render
#method view
from django.core.exceptions import ObjectDoesNotExist
from input_data.models import PenjualanModel
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/") 
def index(request):
    jumlah_hotel = []
    jumlah_mall = []
    jumlah_apartemen = []
    jumlah_c441 = []
    jumlah_c442 = []
    jumlah_c443 = []
    jumlah_c451 = []
    jumlah_c452 = []
    jumlah_c453 = []
    jumlah_c461 = []
    jumlah_c462 = []
    jumlah_c463 = []
    jasa_pembersih_air = []
    jasa_pembersih_kerak_sillica = []
    jasa_pembersih_cooling_tower = []
    jasa_pembersih_stp = []
    jumlah_asam_sulfat = []
    jumlah_molases = []
    jumlah_hcl = []
    jumlah_abf = []
    pendapatan = []
    bulan = []
    labeling = ""
    try:
        years= PenjualanModel.objects.all().order_by('tahun_transaksi')
        year_int = years[len(years) - 1].tahun_transaksi
        labeling="Pendapatan di Tahun " + str(year_int)
    except ObjectDoesNotExist:
        year_int = 0
    
    try:
        data_tahun_sebelumnya = PenjualanModel.objects.filter(tahun_transaksi = year_int)
        for posts in data_tahun_sebelumnya:
            
            jumlah_hotel.append(posts.jumlah_hotel)
            jumlah_mall.append(posts.jumlah_mall)
            jumlah_apartemen.append(posts.jumlah_apartemen)
            jumlah_c441.append(posts.jumlah_C441)
            jumlah_c442.append(posts.jumlah_C442)
            jumlah_c443.append(posts.jumlah_C443)
            jumlah_c451.append(posts.jumlah_C451)
            jumlah_c452.append(posts.jumlah_C452)
            jumlah_c453.append(posts.jumlah_C453)
            jumlah_c461.append(posts.jumlah_C461)
            jumlah_c462.append(posts.jumlah_C462)
            jumlah_c463.append(posts.jumlah_C463)
            jasa_pembersih_air.append(posts.jasa_pembersih_air)
            jasa_pembersih_kerak_sillica.append(posts.jasa_pembersih_kerak_sillica)  
            jasa_pembersih_cooling_tower.append(posts.jasa_pembersih_cooling_tower)
            jasa_pembersih_stp.append(posts.jasa_pembersih_stp)
            jumlah_asam_sulfat.append(posts.jumlah_asam_sulfat)
            jumlah_molases.append(posts.jumlah_molases)
            jumlah_hcl.append(posts.jumlah_hcl)
            jumlah_abf.append(posts.jumlah_abf)
            pendapatan.append(posts.pendapatan)
            
    except ObjectDoesNotExist:
        data_tahun_sebelumnya = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    
    context = {
        'title' : 'Home',
        'jumlah_hotel':  jumlah_hotel,
        'jumlah_mall': jumlah_mall,
        'jumlah_apartemen': jumlah_apartemen,
        'jumlah_c441': jumlah_c441,
        'jumlah_c442': jumlah_c442,
        'jumlah_c443': jumlah_c443,
        'jumlah_c451': jumlah_c451,
        'jumlah_c452': jumlah_c452,
        'jumlah_c453': jumlah_c453,
        'jumlah_c461': jumlah_c461,
        'jumlah_c462': jumlah_c462,
        'jumlah_c463': jumlah_c463,
        'jasa_pembersih_air': jasa_pembersih_air,
        'jasa_pembersih_kerak_sillica': jasa_pembersih_kerak_sillica, 
        'jasa_pembersih_cooling_tower': jasa_pembersih_cooling_tower, 
        'jasa_pembersih_stp': jasa_pembersih_stp,
        'jumlah_asam_sulfat': jumlah_asam_sulfat,
        'jumlah_molases': jumlah_molases,
        'jumlah_hcl': jumlah_hcl,
        'jumlah_abf': jumlah_abf,
        'pendapatan':  pendapatan,
        'labeling': labeling,
       
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
