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
    bulan_tertentu = []
    for posts in post:
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
     
    n = x

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
        jumlah_bulan = 0
        jumlah_penjualan_bulan_tertentu = 0
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

def hitung_data_tahun_sebelumnya(tahuntahunsebelumnya):
    post = PenjualanModel.objects.filter(tahun_transaksi = tahuntahunsebelumnya)
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
    semua = []
    for posts in post:
        # print(posts.jumlah_hotel)
        # print(posts.jumlah_C441)
        
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
    return(semua)
def hitung_forecasting_tahun_sebelumnya(post, index_tahun,  tahuntahunsebelumnya):
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
    index_total_break = []
    for posts in post:
        # print(posts.jumlah_hotel)
        # print(posts.jumlah_C441)
        x += 1
        if(posts.tahun_transaksi == tahuntahunsebelumnya):
            index_total_break.append(x)
            
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
    hitung_bulan = 0
    z = 0
    total_data_y = []
    total_data_y_all = []
    index_musiman =[]
    rata_rata_penjualan_bulan_januari   = []
    rata_rata_penjualan_bulan_februari = []
    rata_rata_penjualan_bulan_maret    = []
    rata_rata_penjualan_bulan_april    = []
    rata_rata_penjualan_bulan_mei      = []
    rata_rata_penjualan_bulan_juni     = []
    rata_rata_penjualan_bulan_juli     = []
    rata_rata_penjualan_bulan_agustus  = []
    rata_rata_penjualan_bulan_september= []
    rata_rata_penjualan_bulan_oktober  = []
    rata_rata_penjualan_bulan_november = []
    rata_rata_penjualan_bulan_desember  = []
    rata_rata_penjualan_bulan_urut = []
    rata_rata_penjualan_bulan_urut_total = []
    jumlah_bulan_januari  = 0
    jumlah_penjualan_bulan_tertentu_januari   = 0 
    jumlah_bulan_februari  = 0
    jumlah_penjualan_bulan_tertentu_februari   = 0 
    jumlah_bulan_maret  = 0
    jumlah_penjualan_bulan_tertentu_maret   = 0 
    jumlah_bulan_april  = 0
    jumlah_penjualan_bulan_tertentu_april  = 0 
    jumlah_bulan_mei = 0
    jumlah_penjualan_bulan_tertentu_mei   = 0 
    jumlah_bulan_juni  = 0
    jumlah_penjualan_bulan_tertentu_juni   = 0 
    jumlah_bulan_juli  = 0
    jumlah_penjualan_bulan_tertentu_juli   = 0 
    jumlah_bulan_agustus  = 0
    jumlah_penjualan_bulan_tertentu_agustus   = 0 
    jumlah_bulan_september= 0
    jumlah_penjualan_bulan_tertentu_september   = 0 
    jumlah_bulan_oktober  = 0
    jumlah_penjualan_bulan_tertentu_oktober   = 0 
    jumlah_bulan_november  = 0
    jumlah_penjualan_bulan_tertentu_november   = 0 
    jumlah_bulan_desember  = 0
    jumlah_penjualan_bulan_tertentu_desember   = 0 
    data_array = 0
    data_array_in_array = 0
    y_index_musiman= 0
    y_index_musiman_produk = []
    y_index_musiman_all = []
    data_tahun_tahun_sebelumnya = []
    data_mape_array = 0
    data_mape_in_array = 0
    data_mape = []
    data_all_mape = []
    array_data_mape = 0
    totat_mape =0
    hasil_keselurahan_mape= []
    for satuan in semua:
        hitung+= 1
        x_y = 0
        xy = 0
        total_xy = 0
        total_y = 0
        b = 0
        a = 0
        y = 0
        hitung_bulan = 0
        rata_rata_penjualan_total = 0
        for satudata in satuan :
            
            x_y += 1
            xy = x_y * satudata
            total_xy = total_xy + xy
            total_y = total_y + satudata
            if(bulan_tertentu[hitung_bulan] == "januari"):
                 jumlah_bulan_januari += 1 
                 jumlah_penjualan_bulan_tertentu_januari += satudata
            if(bulan_tertentu[hitung_bulan] == "februari"):
                 jumlah_bulan_februari += 1 
                 jumlah_penjualan_bulan_tertentu_februari += satudata
            if(bulan_tertentu[hitung_bulan] == "maret"):
                 jumlah_bulan_maret += 1 
                 jumlah_penjualan_bulan_tertentu_maret += satudata
            if(bulan_tertentu[hitung_bulan] == "april"):
                 jumlah_bulan_april += 1 
                 jumlah_penjualan_bulan_tertentu_april += satudata
            if(bulan_tertentu[hitung_bulan] == "mei"):
                 jumlah_bulan_mei += 1 
                 jumlah_penjualan_bulan_tertentu_mei += satudata
            if(bulan_tertentu[hitung_bulan] == "juni"):
                 jumlah_bulan_juni += 1 
                 jumlah_penjualan_bulan_tertentu_juni += satudata
            if(bulan_tertentu[hitung_bulan] == "juli"):
                 jumlah_bulan_juli += 1 
                 jumlah_penjualan_bulan_tertentu_juli += satudata
            if(bulan_tertentu[hitung_bulan] == "agustus"):
                 jumlah_bulan_agustus += 1 
                 jumlah_penjualan_bulan_tertentu_agustus += satudata
            if(bulan_tertentu[hitung_bulan] == "september"):
                 jumlah_bulan_september += 1 
                 jumlah_penjualan_bulan_tertentu_september += satudata
            if(bulan_tertentu[hitung_bulan] == "oktober"):
                 jumlah_bulan_oktober += 1 
                 jumlah_penjualan_bulan_tertentu_oktober += satudata
            if(bulan_tertentu[hitung_bulan] == "november"):
                 jumlah_bulan_november += 1 
                 jumlah_penjualan_bulan_tertentu_november += satudata
            if(bulan_tertentu[hitung_bulan] == "desember"):
                 jumlah_bulan_desember += 1 
                 jumlah_penjualan_bulan_tertentu_desember += satudata
            hitung_bulan += 1
        
        rata_rata_penjualan_total = total_y / x_y
        
        rata_rata_penjualan_bulan_januari   =(  (jumlah_penjualan_bulan_tertentu_januari / jumlah_bulan_januari) / rata_rata_penjualan_total )
        rata_rata_penjualan_bulan_februari  =( (jumlah_penjualan_bulan_tertentu_februari / jumlah_bulan_februari) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_maret     =((jumlah_penjualan_bulan_tertentu_maret / jumlah_bulan_maret) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_april     =(  (jumlah_penjualan_bulan_tertentu_april / jumlah_bulan_april) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_mei       =( (jumlah_penjualan_bulan_tertentu_mei / jumlah_bulan_mei) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_juni      =(  (jumlah_penjualan_bulan_tertentu_juni / jumlah_bulan_juni) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_juli      =(  (jumlah_penjualan_bulan_tertentu_juli / jumlah_bulan_juli) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_agustus   =(  (jumlah_penjualan_bulan_tertentu_agustus / jumlah_bulan_agustus) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_september =( (jumlah_penjualan_bulan_tertentu_september / jumlah_bulan_september) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_oktober   =(  (jumlah_penjualan_bulan_tertentu_oktober / jumlah_bulan_oktober) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_november  =(  (jumlah_penjualan_bulan_tertentu_november / jumlah_bulan_november) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_desember  =( (jumlah_penjualan_bulan_tertentu_desember / jumlah_bulan_desember) / rata_rata_penjualan_total)
        rata_rata_penjualan_bulan_urut= [
            rata_rata_penjualan_bulan_januari,  
            rata_rata_penjualan_bulan_februari, 
            rata_rata_penjualan_bulan_maret,    
            rata_rata_penjualan_bulan_april,    
            rata_rata_penjualan_bulan_mei,      
            rata_rata_penjualan_bulan_juni,     
            rata_rata_penjualan_bulan_juli,     
            rata_rata_penjualan_bulan_agustus,  
            rata_rata_penjualan_bulan_september,
            rata_rata_penjualan_bulan_oktober,  
            rata_rata_penjualan_bulan_november, 
            rata_rata_penjualan_bulan_desember
        ]
        rata_rata_penjualan_bulan_urut_total.append(rata_rata_penjualan_bulan_urut)
        jumlah_bulan_januari  = 0
        jumlah_penjualan_bulan_tertentu_januari   = 0 
        jumlah_bulan_februari  = 0
        jumlah_penjualan_bulan_tertentu_februari   = 0 
        jumlah_bulan_maret  = 0
        jumlah_penjualan_bulan_tertentu_maret   = 0 
        jumlah_bulan_april  = 0
        jumlah_penjualan_bulan_tertentu_april  = 0 
        jumlah_bulan_mei = 0
        jumlah_penjualan_bulan_tertentu_mei   = 0 
        jumlah_bulan_juni  = 0
        jumlah_penjualan_bulan_tertentu_juni   = 0 
        jumlah_bulan_juli  = 0
        jumlah_penjualan_bulan_tertentu_juli   = 0 
        jumlah_bulan_agustus  = 0
        jumlah_penjualan_bulan_tertentu_agustus   = 0 
        jumlah_bulan_september= 0
        jumlah_penjualan_bulan_tertentu_september   = 0 
        jumlah_bulan_oktober  = 0
        jumlah_penjualan_bulan_tertentu_oktober   = 0 
        jumlah_bulan_november  = 0
        jumlah_penjualan_bulan_tertentu_november   = 0 
        jumlah_bulan_desember  = 0
        jumlah_penjualan_bulan_tertentu_desember   = 0 
        
        # index_musiman.append(rata_rata_penjualan_bulan_tertentu / rata_rata_penjualan_total)
        
        # rata_rata_penjualan_bulan_january = jumlah_penjualan_bulan_january/ jumlah_penjualan_bulan_january   
        
        
                
        # y_index_musiman.append(round(y * index_musiman)) 
        b = ((n * total_xy)-(total_x * total_y)) / ((n * x_kuadrat) - (total_x * total_x))
        a = (total_y - (b * total_x))/n
        for z in range(len(index_total_break)):    
            y = a + (b * index_total_break[z])
           

            total_data_y.append(y)
            
            
        total_data_y_all.append(total_data_y)
        total_data_y = []
        
    for data_array in range(len(total_data_y_all)):
        data_satu_y = total_data_y_all[data_array]
        data_satu_index_musim = rata_rata_penjualan_bulan_urut_total[data_array]
        
        for data_array_in_array in range( 12 ):
            y_index_musiman = data_satu_y[data_array_in_array] * data_satu_index_musim[data_array_in_array]
             
            y_index_musiman_produk.append(y_index_musiman) 
        y_index_musiman_all.append(y_index_musiman_produk)
        
        y_index_musiman_produk = []
    print(len(y_index_musiman_all))
    data_tahun_tahun_sebelumnya = hitung_data_tahun_sebelumnya(tahuntahunsebelumnya)
    data_mape_array = 0
    for data_mape_array in range(len(data_tahun_tahun_sebelumnya)):
        data_index_satu = y_index_musiman_all[data_mape_array]
        data_tahun_sebelumnya_satu = data_tahun_tahun_sebelumnya[data_mape_array]
        total_mape = 0
        data_mape = []

        for data_mape_in_array in range(len(data_index_satu)):
            mape = ((data_index_satu[data_mape_in_array] - data_tahun_sebelumnya_satu [data_mape_in_array])/ data_tahun_sebelumnya_satu[data_mape_in_array])
            data_mape.append(abs(mape))
        for datainmape in data_mape:
            total_mape += datainmape
        hasil_mape = (total_mape / 12) * 100
        hasil_keselurahan_mape.append(hasil_mape)
    return(hasil_keselurahan_mape)

def index_musim(semua_data, bulan_tertentu):
    xzz = 0
    penjualan_januari = 0
    penjualan_februari = 0
    penjualan_maret = 0
    penjualan_april = 0
    penjualan_mei = 0
    penjualan_juni = 0
    penjualan_juli = 0
    penjualan_agustus = 0
    penjualan_september = 0
    penjualan_oktober = 0
    penjualan_november = 0
    penjualan_desember = 0
    index_januari = 0
    index_februari = 0
    index_maret = 0
    index_april = 0
    index_mei = 0
    index_juni = 0
    index_juli = 0
    index_agustus = 0
    index_september = 0
    index_oktober = 0
    index_november = 0
    index_desember = 0
    bulan_tertentu_keseluruhan =[]
    for semua in semua_data:
        xzz = 0
        penjualan_januari = 0
        penjualan_februari = 0
        penjualan_maret = 0
        penjualan_april = 0
        penjualan_mei = 0
        penjualan_juni = 0
        penjualan_juli = 0
        penjualan_agustus = 0
        penjualan_september = 0
        penjualan_oktober = 0
        penjualan_november = 0
        penjualan_desember = 0
        index_januari = 0
        index_februari = 0
        index_maret = 0
        index_april = 0
        index_mei = 0
        index_juni = 0
        index_juli = 0
        index_agustus = 0
        index_september = 0
        index_oktober = 0
        index_november = 0
        index_desember = 0
        penjualan_bulan_tertentu=[]
        satu_data_seluruhan=0
        for satudata in semua:
            if(bulan_tertentu[xzz] == 'januari'):
                penjualan_januari+= satudata
                index_januari += 1
            if(bulan_tertentu[xzz] == 'februari'):
                penjualan_februari+= satudata
                index_februari +=1
            if(bulan_tertentu[xzz] == 'maret'):
                penjualan_maret+= satudata
                index_maret +=1
            if(bulan_tertentu[xzz] == 'april'):
                penjualan_april+= satudata
                index_april += 1
            if(bulan_tertentu[xzz] == 'mei'):
                penjualan_mei+= satudata
                index_mei += 1
            if(bulan_tertentu[xzz] == 'juni'):
                penjualan_juni+= satudata
                index_juni += 1
            if(bulan_tertentu[xzz] == 'juli'):
                penjualan_juli+= satudata
                index_juli +=1
            if(bulan_tertentu[xzz] == 'agustus'):
                penjualan_agustus+= satudata
                index_agustus +=1
            if(bulan_tertentu[xzz] == 'september'):
                penjualan_september+= satudata
                index_september +=1
            if(bulan_tertentu[xzz] == 'oktober'):
                penjualan_oktober+= satudata
                index_oktober +=1
            if(bulan_tertentu[xzz] == 'november'):
                penjualan_november+= satudata
                index_november +=1
            if(bulan_tertentu[xzz] == 'desember'):
                index_desember +=1
                penjualan_desember+= satudata
            xzz += 1
            satu_data_seluruhan += satudata

        penjualan_bulan_tertentu= [(penjualan_januari/index_januari)/(satu_data_seluruhan/xzz), (penjualan_februari/index_februari)/(satu_data_seluruhan/xzz), (penjualan_maret/index_maret)/(satu_data_seluruhan/xzz), (penjualan_april/index_april)/(satu_data_seluruhan/xzz) ,
        (penjualan_mei/index_mei)/(satu_data_seluruhan/xzz), (penjualan_juni/index_juni)/(satu_data_seluruhan/xzz), (penjualan_juli/index_juli)/(satu_data_seluruhan/xzz), (penjualan_agustus/index_agustus)/(satu_data_seluruhan/xzz), (penjualan_september/index_september)/(satu_data_seluruhan/xzz), (penjualan_oktober/index_oktober)/(satu_data_seluruhan/xzz),
        (penjualan_november/index_november)/(satu_data_seluruhan/xzz), (penjualan_desember/index_desember)/(satu_data_seluruhan/xzz)]
        bulan_tertentu_keseluruhan.append(penjualan_bulan_tertentu)
    
    return(bulan_tertentu_keseluruhan)
def hitung_forecasting_tahun(post, si_x):
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
    xx = 0
    hitung_x = 0
    semua_data = []
    semua_semua_data =[]
    index_musim_keseluruhan = index_musim(semua, bulan_tertentu)
    index_musim_satuan = []
    index_musim_penghitung = 0
    for satuan in semua:
        hitung+= 1
        x_y = 0
        xy = 0
        total_xy = 0
        total_y = 0
        b = 0
        a = 0
        y = 0
        xx = 0
        hitung_x = 0
        semua_data = []
        index_musim_satuan = index_musim_keseluruhan[index_musim_penghitung]
        index_musim_penghitung +=1
        xzz = 0
        for satudata in satuan :
            x_y += 1
            xy = x_y * satudata
            total_xy = total_xy + xy
            total_y = total_y + satudata
         
        b = ((n * total_xy)-(total_x * total_y)) / ((n * x_kuadrat) - (total_x * total_x))
        a = (total_y - (b * total_x))/n
        
        for xx in range(12):
            xx+=1
            hitung_x = si_x + xx
            y = a + (b * (hitung_x + x_y))
            # print((hitung_x + x_y))
            # print(hitung_x + x_y)
            y = round(y * index_musim_satuan[xzz])
            # print(index_musim_satuan[xzz])
            xzz+=1
            
            semua_data.append(y)
        semua_semua_data.append(semua_data)
    return(semua_semua_data)
@login_required(login_url="/accounts/login/")   
def index(request):
    post = PenjualanModel.objects.all()
    post_tahun = PenjualanModel.objects.values_list('tahun_transaksi', flat=True).distinct()
    tahuntambahan = 1
    tahunterakhir = post_tahun[len(post_tahun)-1] 
    tahun = []
    for tahuntambahan in range(10):
        tahun.append(tahunterakhir+tahuntambahan)
    tahun.reverse()
    dating_form = forms.DatingForm()
  

    context = {
        'heading':'Forecasting',
        'dating_form': dating_form,
        'tahun': tahun,
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
        hasilsebelumnya = []
        hitungmape= []
        allhasilmape =[]
        hasilakhirmape = 0
        testhasilmape = []
        pesan = ""
        y = 0
        z= 0
        bulan = request.POST['bulan_dan_tahun_prediksi_month'] 
        tahun = request.POST['bulan_dan_tahun_prediksi_year']   
        if(bulan != '0' and tahun != '0'):
            index_tahun = ((int(tahun) - year_int - 1) * 12)
            si_x = index_tahun + (int(request.POST['bulan_dan_tahun_prediksi_month'] ))
            si_y = index_tahun + (int(request.POST['bulan_dan_tahun_prediksi_month'] )) - 1
            hasilnya=(hitung_forecasting(post, index_tahun, si_x, thismonth, bulan))
            hasilsebelumnya=(hitung_forecasting(post, index_tahun, si_x, thismonth, bulan))
            if int(tahun) == year_int:
                tahuntahunsebelumnya = year_int
                testhasilmape = hitung_forecasting_tahun_sebelumnya(post, index_tahun,  tahuntahunsebelumnya)
                for hasil in testhasilmape :
                    hasilakhirmape = hasilakhirmape + hasil
                   
                hasilakhirmape = round((hasilakhirmape / len(testhasilmape)),3)
                pesan = "Persentase Error(MAPE) Pada Tahun "+tahun+ " adalah " + str(hasilakhirmape)+"%"
            else:
                pesan = "Belum Ada Data Asli Pada tahun "+tahun + " Sehingga Tidak Memiliki Persentase Error(MAPE)"
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

        # if len(hasilnya) != 0 :
        #     for y in range(len(hasilnya)-1):
        #         selisihdata = round((hasilnya[y] - data_all_tahun_sebelumnya[y])/data_all_tahun_sebelumnya[y], 3)
        #         hitungmape = round(((hasilnya[y]-data_all_tahun_sebelumnya[y])/data_all_tahun_sebelumnya[y])*100, 3)
        #         hasilakhirmape += abs(hitungmape)
        #         presentasidata.append(selisihdata)
        #         allhasilmape.append(abs(hitungmape))
            
        #     hasilakhirmape = round(hasilakhirmape / (len(hasilnya)-1),3)
            
        labeling = "Hasil Prediksi Penjualan pada bulan " +thismonth[bulan]+ " tahun " + tahun    
        labeling2 = "Hasil Penjualan pada bulan " + thismonth[bulan] + " tahun " + str(year_int)
        tahunpredict = int(tahun)
        tahunprediksii = [tahunpredict]
        del hasilnya[-1]
        del data_all_tahun_sebelumnya[-1]    
        
        # informasidata = ["jumlah client hotel", "jumlah client mall", "jumlah client apartemen", "C441 Terjual", "C442 Terjual", "C443 Terjual", "C451 Terjual", "C452 Terjual", "C453 Terjual", "C461 Terjual", "C462 Terjual", "C463 Terjual", "Jasa Pembersih Air", "Jasa Pembersih Kerak Sillica", "Jasa Pembersih Cooling Tower", "Jasa Pembersih STP", "Asam Sulfat Terpakai", "Molases Terpakai", "HCL Terpakai", "ABF Terpakai", "pendapatan"]           
        # infodata = dict([informasidata[z], [presentasidata[z], round(testhasilmape[z],3)]] for z in range(len(informasidata)-1))
        
        context = {
        'heading':'Forecasting',
        'datas': hasilnya,
        'data_sebelumnya': data_all_tahun_sebelumnya,
        'labeling': labeling,
        'labeling2': labeling2,
        'tahunprediksii': tahunprediksii,
        'pendapatanasli': pendapatanasli,
        'pendapatanpredict': pendapatanpredict,
        # 'infodata': infodata,
        'tahunterakhir': year_int,
        'pesan': pesan,
        # 'data_form':contact_form,
        # 'posts' : post,

         }
    else:
       return redirect('forecasting:index')
    
    return render(request, 'forecasting/forecasting.html', context)



def resultForecastingTahun(request):
    hasilprediksi = []
    if request.method == 'POST':
        try:
            years= PenjualanModel.objects.all().order_by('tahun_transaksi')
            year_int = years[len(years) - 1].tahun_transaksi
        except ObjectDoesNotExist:
            year_int = 0
        tahun = request.POST['tahun']  
        post = PenjualanModel.objects.all()
        index_tahun = ((int(tahun) - year_int - 1) * 12)
        hasilprediksi = hitung_forecasting_tahun(post, index_tahun)
        hasilakhirmape = 0
        pesan = ""
        if int(tahun) == year_int:
                tahuntahunsebelumnya = year_int
                testhasilmape = hitung_forecasting_tahun_sebelumnya(post, index_tahun,  tahuntahunsebelumnya)
                for hasil in testhasilmape :
                    hasilakhirmape = hasilakhirmape + hasil
                   
                hasilakhirmape = round((hasilakhirmape / len(testhasilmape)),3)
                pesan = "Persentase Error(MAPE) Pada Tahun "+tahun+ " adalah " + str(hasilakhirmape)+"%"
        else:
                pesan = "Belum Ada Data Asli Pada tahun "+tahun + " Sehingga Tidak Memiliki Persentase Error(MAPE)"
    context = {
        'heading':'Forecasting',
        'hasilprediksi': hasilprediksi,
        'tahun': int(tahun),
        'pesan': pesan,
    }


    return render(request, 'forecasting/forecastingtahun.html', context)
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

