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
                    dataall.append(selisihdata)
            del datatahunsatu[-1]
            del datatahundua[-1]
            informasidata = ["jumlah client hotel", "jumlah client mall", "jumlah client apartemen", "C441 Terjual", "C442 Terjual", "C443 Terjual", "C451 Terjual", "C452 Terjual", "C453 Terjual", "C461 Terjual", "C462 Terjual", "C463 Terjual", "Jasa Pembersih Air", "Jasa Pembersih Kerak Sillica", "Jasa Pembersih Cooling Tower", "Jasa Pembersih STP", "Asam Sulfat Terpakai", "Molases Terpakai", "HCL Terpakai", "ABF Terpakai", "pendapatan"]           
            infodata = dict([informasidata[z], dataall[z]] for z in range(len(informasidata)-1))
            print(infodata)
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