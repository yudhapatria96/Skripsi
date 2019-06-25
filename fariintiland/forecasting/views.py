from django.shortcuts import render, redirect
from input_data.models import PenjualanModel
from . import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
# from . import forms
# from . import models

def hitung_forecasting(post, index_tahun, si_x, thismonth, bulan):
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
    bulan_tertentu = []
    semua = []
    x = 0
    x_kuadrat = 0
    total_x = 0
    b = 0 
    a = 0
    n = 0
    jumlah_bulan = 0
    y_index_musiman= []
    rata_rata_penjualan_bulan_tertentu = 0 
    jumlah_penjualan_bulan_tertentu = 0
    rata_rata_penjualan_total = 0
    index_musiman = 0
    for posts in post:
        # print(posts.jumlah_hotel)
        # print(posts.jumlah_C441)
        x += 1
        x_kuadrat = x_kuadrat + (x * x)
        total_x = total_x + x
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
        bulan_tertentu.append(posts.bulan_transaksi)
        # if(thismonth[bulan] == posts.bulan_transaksi):
        #     jumlah_bulan += 1       
    n = x
    # print(jasa_pembersih_air)
    # print(x_kuadrat)
    # print(total_x)
    # print(x)
        
    semua = [jumlah_hotel, jumlah_mall,jumlah_apartemen,jumlah_c441,jumlah_c442,
    jumlah_c443,jumlah_c451,jumlah_c452,jumlah_c453,jumlah_c461,jumlah_c462,jumlah_c463,
    jasa_pembersih_air,
    jasa_pembersih_kerak_sillica,
    jasa_pembersih_cooling_tower,
    jasa_pembersih_stp,
    jumlah_asam_sulfat,
    jumlah_molases,
    jumlah_hcl,
    jumlah_abf, pendapatan]
    hitung = 0
    for satuan in semua:
        hitung+= 1
        x_y = 0
        xy = 0
        total_xy = 0
        total_y = 0
        b = 0
        a = 0
        y = 0
        for satudata in satuan :
            if(thismonth[bulan] == bulan_tertentu[x_y]):
               jumlah_bulan += 1 
               jumlah_penjualan_bulan_tertentu += satudata
            x_y += 1
            xy = x_y * satudata
            total_xy = total_xy + xy
            total_y = total_y + satudata
         
        b = ((n * total_xy)-(total_x * total_y)) / ((n * x_kuadrat) - (total_x * total_x))
        a = (total_y - (b * total_x))/n
        y = a + (b * (si_x + x_y))   
               
        rata_rata_penjualan_bulan_tertentu = jumlah_penjualan_bulan_tertentu / jumlah_bulan
        rata_rata_penjualan_total = total_y / x_y
        
        index_musiman = rata_rata_penjualan_bulan_tertentu / rata_rata_penjualan_total
        y_index_musiman.append(round(y * index_musiman))
    
    return(y_index_musiman)

@login_required(login_url="/accounts/login/")   
def index(request):
    post = PenjualanModel.objects.all()
 
    
    dating_form = forms.DatingForm()
  

    context = {
        'heading':'Forecasting',
        'dating_form': dating_form,
    } 
  
                
    return render(request, 'forecasting/index.html',context)

@login_required(login_url="/accounts/login/")
def resultForecasting(request):
    
    if request.method == 'POST':
        post = PenjualanModel.objects.all()
        hasilnya = 0
        thismonth= {
            '1' : "januari",
            '2' : "februari",
            '3' : "maret",
            '4' : "april",
            '5' : "mei",
            '6' : "juni",
            '7' : "juli",
            '8' : "agustus",
            '9' : "september",
            '10' : "oktober",
            '11' : "november",
            '12' : "desember"
        }
        try:
            years= PenjualanModel.objects.all().order_by('tahun_transaksi')
            year_int = years[len(years) - 1].tahun_transaksi
        except ObjectDoesNotExist:
            year_int = 0
        index_tahun = 0
        y_index_musiman = []
        labels = []
        hasilnya = []
        pendapatanpredict = 0
        pendapatanasli = 0
        data_tahun_sebelumnya = []
        data_all_tahun_sebelumnya = []
        panjangdata = 0
        presentasidata = []
        selisihdata = 0
        infodata = {}
        hitungmape= []
        y = 0
        z= 0
        bulan = request.POST['bulan_dan_tahun_prediksi_month'] 
        tahun = request.POST['bulan_dan_tahun_prediksi_year']   
        if(bulan != '0' and tahun != '0'):
            index_tahun = ((int(tahun) - year_int - 1) * 12)
            si_x = index_tahun + (int(request.POST['bulan_dan_tahun_prediksi_month'] ))
            hasilnya=(hitung_forecasting(post, index_tahun, si_x, thismonth, bulan))
            pendapatanpredict = hasilnya[-1]
            #terakhir ngitung mape
            
        else:
            return redirect('forecasting:index')
        try:
            data_tahun_sebelumnya = PenjualanModel.objects.get(bulan_transaksi = thismonth[bulan], tahun_transaksi = year_int)
            data_all_tahun_sebelumnya = [data_tahun_sebelumnya.jumlah_hotel, data_tahun_sebelumnya.jumlah_mall, data_tahun_sebelumnya.jumlah_apartemen,
            data_tahun_sebelumnya.jumlah_C441, data_tahun_sebelumnya.jumlah_C442, data_tahun_sebelumnya.jumlah_C443, data_tahun_sebelumnya.jumlah_C451,
            data_tahun_sebelumnya.jumlah_C452, data_tahun_sebelumnya.jumlah_C453, data_tahun_sebelumnya.jumlah_C461, data_tahun_sebelumnya.jumlah_C462, 
            data_tahun_sebelumnya.jumlah_C463, data_tahun_sebelumnya.jasa_pembersih_air, data_tahun_sebelumnya.jasa_pembersih_kerak_sillica,
            data_tahun_sebelumnya.jasa_pembersih_cooling_tower, data_tahun_sebelumnya.jasa_pembersih_stp, data_tahun_sebelumnya.jumlah_asam_sulfat,
            data_tahun_sebelumnya.jumlah_molases, data_tahun_sebelumnya.jumlah_hcl, data_tahun_sebelumnya.jumlah_abf, data_tahun_sebelumnya.pendapatan]
            pendapatanasli = data_all_tahun_sebelumnya[-1]
            
        except ObjectDoesNotExist:
            data_tahun_sebelumnya = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        if len(hasilnya) != 0 :
            for y in range(len(hasilnya)-1):
                selisihdata = round((hasilnya[y] - data_all_tahun_sebelumnya[y])/data_all_tahun_sebelumnya[y], 3)
                presentasidata.append(selisihdata)
        labeling = "Hasil Prediksi Penjualan pada bulan " +thismonth[bulan]+ " tahun " + tahun    
        labeling2 = "Hasil Penjualan pada bulan " + thismonth[bulan] + " tahun " + str(year_int)
        tahunpredict = int(tahun)
        tahunprediksii = [ year_int,tahunpredict]
        del hasilnya[-1]
        del data_all_tahun_sebelumnya[-1]    
        
        informasidata = ["jumlah client hotel", "jumlah client mall", "jumlah client apartemen", "C441 Terjual", "C442 Terjual", "C443 Terjual", "C451 Terjual", "C452 Terjual", "C453 Terjual", "C461 Terjual", "C462 Terjual", "C463 Terjual", "Jasa Pembersih Air", "Jasa Pembersih Kerak Sillica", "Jasa Pembersih Cooling Tower", "Jasa Pembersih STP", "Asam Sulfat Terpakai", "Molases Terpakai", "HCL Terpakai", "ABF Terpakai", "pendapatan"]           
        infodata = dict([informasidata[z], presentasidata[z]] for z in range(len(informasidata)-1))
        
        context = {
        'heading':'Forecasting',
        'datas': hasilnya,
        'data_sebelumnya': data_all_tahun_sebelumnya,
        'labeling': labeling,
        'labeling2': labeling2,
        'tahunprediksii': tahunprediksii,
        'pendapatanasli': pendapatanasli,
        'pendapatanpredict': pendapatanpredict,
        'infodata': infodata,
        # 'data_form':contact_form,
        # 'posts' : post,

         }
    else:
       return redirect('forecasting:index')
    
    return render(request, 'forecasting/forecasting.html', context)

# class ListForecasting(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self,request, format= None):
#         labels = ["jumlah hotel", "jumlah mall", "jumlah apartemen", "C441 Terjual", "C442 Terjual", "C443 Terjual", "C451 Terjual", "C452 Terjual", "C453 Terjual", "C461 Terjual", "C462 Terjual", "C463 Terjual", "Jasa Pembersih Air", "Jasa Pembersih Cooling Tower", "Jasa Pembersih STP", "Asam Sulfat Terpakai", "Molases Terpakai", "HCL Terpakai", "ABF Terpakai"]           
#         data_forecast = [123 ,123 ,123 ,321,242,25,262,272,282,2942,21,245,262,141,242,232,252,262]
#         data = {
#             "sales": 100,
#             "labels": labels,
#             "data_prediksi": data_forecast,
#             "customers": 10,
#         }
        
#         return Response(data)