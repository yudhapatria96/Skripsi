from django.shortcuts import render, redirect
from input_data.models import PenjualanModel
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def index(request):

    post_tahun = PenjualanModel.objects.values_list('tahun_transaksi', flat=True).distinct()

    
    context = {
        'heading':'Forecasting',
        'tahun': post_tahun,
        
    } 
  
                
    return render(request, 'komparasi/index.html',context)

@login_required(login_url="/accounts/login/")
def indextahun(request):

    post_tahun = PenjualanModel.objects.values_list('tahun_transaksi', flat=True).distinct()

    
    context = {
        'heading':'Forecasting',
        'tahun': post_tahun,
        
    } 
  
                
    return render(request, 'komparasi/indextahun.html',context)

@login_required(login_url="/accounts/login/")
def hasilKomparasi(request):

    if request.method == 'POST':
        bulansatu = request.POST['bulansatu'] 
        tahunsatu = request.POST['tahunsatu']  
        bulandua = request.POST['bulandua'] 
        tahundua = request.POST['tahundua']
        datatahunsatu = []
        datatahundua  = []
        dataPelangganSatu = []
        dataPelangganDua = []
        dataC44Satu = []
        dataC44Dua = []
        dataC45Satu = []
        dataC45Dua = []
        dataC46Satu = []
        dataC46Dua = []
        dataJasaSatu = []
        dataJasaDua = []
        dataBahanSatu = []
        dataBahanDua = []
        tahunall = []
        labeling1 = ""
        labeling2 = ""
        pendapatansatu = 0
        pendapatandua = 0
        dataall = []
        selisihdata = 0
        y= 0
        if bulansatu != "0" and tahunsatu != "0" and bulandua !="0" and tahundua != "0":
            try:
                datasatu            = PenjualanModel.objects.get(bulan_transaksi = bulansatu, tahun_transaksi = tahunsatu)
                datatahunsatu       = [datasatu.jumlah_hotel, datasatu.jumlah_mall, datasatu.jumlah_apartemen,
                                        datasatu.jumlah_C441, datasatu.jumlah_C442, datasatu.jumlah_C443, datasatu.jumlah_C451,
                                        datasatu.jumlah_C452, datasatu.jumlah_C453, datasatu.jumlah_C461, datasatu.jumlah_C462, 
                                        datasatu.jumlah_C463, datasatu.jasa_pembersih_air, datasatu.jasa_pembersih_kerak_sillica,
                                        datasatu.jasa_pembersih_cooling_tower, datasatu.jasa_pembersih_stp, datasatu.jumlah_asam_sulfat,
                                        datasatu.jumlah_molases, datasatu.jumlah_hcl, datasatu.jumlah_abf, datasatu.pendapatan]
                dataPelangganSatu   = [datasatu.jumlah_hotel, datasatu.jumlah_mall, datasatu.jumlah_apartemen]
                dataC44Satu         = [datasatu.jumlah_C441, datasatu.jumlah_C442, datasatu.jumlah_C443 ]
                dataC45Satu         = [datasatu.jumlah_C451, datasatu.jumlah_C452, datasatu.jumlah_C453 ]
                dataC46Satu         = [datasatu.jumlah_C461, datasatu.jumlah_C462, datasatu.jumlah_C463]
                dataJasaSatu        = [datasatu.jasa_pembersih_air, datasatu.jasa_pembersih_kerak_sillica, datasatu.jasa_pembersih_cooling_tower, datasatu.jasa_pembersih_stp, datasatu.jumlah_asam_sulfat]
                dataBahanSatu       = [datasatu.jumlah_asam_sulfat, datasatu.jumlah_molases, datasatu.jumlah_hcl, datasatu.jumlah_abf ]
                pendapatansatu = datasatu.pendapatan
                tahunall=[int(tahunsatu),int(tahundua)]
            except ObjectDoesNotExist:
                datatahunsatu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            try:
                datadua             = PenjualanModel.objects.get(bulan_transaksi = bulandua, tahun_transaksi = tahundua)
                datatahundua        = [datadua.jumlah_hotel, datadua.jumlah_mall, datadua.jumlah_apartemen,
                                      datadua.jumlah_C441, datadua.jumlah_C442, datadua.jumlah_C443, datadua.jumlah_C451,
                                      datadua.jumlah_C452, datadua.jumlah_C453, datadua.jumlah_C461, datadua.jumlah_C462, 
                                      datadua.jumlah_C463, datadua.jasa_pembersih_air, datadua.jasa_pembersih_kerak_sillica,
                                      datadua.jasa_pembersih_cooling_tower, datadua.jasa_pembersih_stp, datadua.jumlah_asam_sulfat,
                                      datadua.jumlah_molases, datadua.jumlah_hcl, datadua.jumlah_abf, datadua.pendapatan]
                dataPelangganDua    = [datadua.jumlah_hotel, datadua.jumlah_mall, datadua.jumlah_apartemen]
                dataC44Dua          = [ datadua.jumlah_C441, datadua.jumlah_C442, datadua.jumlah_C443]
                dataC45Dua          = [datadua.jumlah_C451,datadua.jumlah_C452, datadua.jumlah_C453]
                dataC46Dua          = [datadua.jumlah_C461, datadua.jumlah_C462, datadua.jumlah_C463]
                dataJasaDua         = [datadua.jasa_pembersih_air, datadua.jasa_pembersih_kerak_sillica, datadua.jasa_pembersih_cooling_tower, datadua.jasa_pembersih_stp]
                dataBahanDua        =  [datadua.jumlah_asam_sulfat, datadua.jumlah_molases, datadua.jumlah_hcl, datadua.jumlah_abf]
                pendapatandua       = datadua.pendapatan
            except ObjectDoesNotExist:
                datatahundua = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            
            if len(datatahunsatu) !=0:
                for y in range(len(datatahunsatu)-1):
                    selisihdata = round((datatahundua[y] - datatahunsatu[y])/datatahunsatu[y], 3)
                    selisihdata = selisihdata * 100
                    dataall.append(selisihdata)
            del datatahunsatu[-1]
            del datatahundua[-1]
            informasidata = ["jumlah client hotel", "jumlah client mall", "jumlah client apartemen", "C441 Terjual", "C442 Terjual", "C443 Terjual", "C451 Terjual", "C452 Terjual", "C453 Terjual", "C461 Terjual", "C462 Terjual", "C463 Terjual", "Jasa Pembersih Air", "Jasa Pembersih Kerak Sillica", "Jasa Pembersih Cooling Tower", "Jasa Pembersih STP", "Asam Sulfat Terpakai", "Molases Terpakai", "HCL Terpakai", "ABF Terpakai", "pendapatan"]           
            infodata = dict([informasidata[z], dataall[z]] for z in range(len(informasidata)-1))
            labeling1  = "Hasil Penjualan pada bulan " +bulansatu+ " tahun " + tahunsatu    
            labeling2 = "Hasil Penjualan pada bulan " + bulandua + " tahun " + tahundua
        else:
            return redirect('komparasi:index')
    
        context = {
            'heading':'Forecasting',
            'datatahunsatu': datatahunsatu,
            'datatahundua': datatahundua, 
            'labeling1' : labeling1,
            'labeling2' : labeling2,
            'dataPelangganSatu' : dataPelangganSatu,
            'dataC44Satu'      :dataC44Satu,      
            'dataC45Satu'      :dataC45Satu,      
            'dataC46Satu'      :dataC46Satu,      
            'dataJasaSatu'     :dataJasaSatu,     
            'dataBahanSatu'    :dataBahanSatu,
            'dataPelangganDua' : dataPelangganDua,
            'dataC44Dua'      :dataC44Dua,      
            'dataC45Dua'      :dataC45Dua,      
            'dataC46Dua'      :dataC46Dua,      
            'dataJasaDua'     :dataJasaDua,     
            'dataBahanDua'    :dataBahanDua,  
            'pendapatansatu'  :pendapatansatu,
            'pendapatandua'   :pendapatandua,
            'infodata': infodata,
            'tahunall': tahunall,
        } 
    else:
        return redirect('komparasi:index')
                
    return render(request, 'komparasi/komparasi.html',context)

@login_required(login_url="/accounts/login/")
def hasilKomparasiTahun(request):

    if request.method == 'POST':
        tahunsatu = request.POST['tahunsatu']  
        tahundua = request.POST['tahundua']
       
        tahunall = []
       
        selisihdata = 0
        y= 0
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
        semuasatu = []
        semuasatusatu = []
        semuadua = []
        semuaduadua = []     
        semuaselisihdata = []    
        if  tahunsatu != "0"  and tahundua != "0":
            try:
                datasatu = PenjualanModel.objects.filter(tahun_transaksi = tahunsatu)
                
                for posts in datasatu:
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
                semuasatu = [jumlah_hotel, jumlah_mall,jumlah_apartemen,jumlah_c441,jumlah_c442,
                jumlah_c443,jumlah_c451,jumlah_c452,jumlah_c453,jumlah_c461,jumlah_c462,jumlah_c463,
                jasa_pembersih_air,
                jasa_pembersih_kerak_sillica,
                jasa_pembersih_cooling_tower,
                jasa_pembersih_stp,
                jumlah_asam_sulfat,
                jumlah_molases,
                jumlah_hcl,
                jumlah_abf, pendapatan]
                      
                
                    # tahunall=[int(tahunsatu),int(tahundua)]
            except ObjectDoesNotExist:
                datatahunsatu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            try:
                datadua             = PenjualanModel.objects.filter(tahun_transaksi = tahundua)
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
                for posts in datadua:
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
                semuadua = [jumlah_hotel, jumlah_mall,jumlah_apartemen,jumlah_c441,jumlah_c442,
                jumlah_c443,jumlah_c451,jumlah_c452,jumlah_c453,jumlah_c461,jumlah_c462,jumlah_c463,
                jasa_pembersih_air,
                jasa_pembersih_kerak_sillica,
                jasa_pembersih_cooling_tower,
                jasa_pembersih_stp,
                jumlah_asam_sulfat,
                jumlah_molases,
                jumlah_hcl,
                jumlah_abf, pendapatan]    
                    
            except ObjectDoesNotExist:
                datatahundua = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            
            tahunall=[int(tahunsatu),int(tahundua)]
        else:
            return redirect('komparasi:index')
        y = 0
        z = 0
        if len(semuasatu) != 0 and len(semuadua) != 0:
                for y in range(len(semuasatu)-1):
                    semuasatusatu = semuasatu[y]
                    semuaduadua  = semuadua[y]
                    selisihdata = []
                    selisih = []
                    for z in range(len(semuasatusatu)):
                        selisihdata= (round(((semuaduadua[z] - semuasatusatu[z])/semuasatusatu[z]), 3 ))
                        selisihdata = round(selisihdata * 100 , 3)
                        selisih.append(selisihdata)
                    semuaselisihdata.append(selisih)
                informasidata = ["jumlah client hotel", "jumlah client mall", "jumlah client apartemen", "C441 Terjual", "C442 Terjual", "C443 Terjual", "C451 Terjual", "C452 Terjual", "C453 Terjual", "C461 Terjual", "C462 Terjual", "C463 Terjual", "Jasa Pembersih Air", "Jasa Pembersih Kerak Sillica", "Jasa Pembersih Cooling Tower", "Jasa Pembersih STP", "Asam Sulfat Terpakai", "Molases Terpakai", "HCL Terpakai", "ABF Terpakai", "pendapatan"]           
                infodata = dict([informasidata[z], semuaselisihdata[z]] for z in range(len(informasidata)-1))        
        context = {
            'semuasatu': semuasatu,
            'semuadua': semuadua,
            'tahunall': tahunall,
            'infodata': infodata,
            'tahunsatu' : int(tahunsatu),
            'tahundua' : int(tahundua),
        } 
    else:
        return redirect('komparasi:index')
                
    return render(request, 'komparasi/komparasitahun.html',context)