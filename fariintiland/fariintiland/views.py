# from django.http import HttpResponse
from django.shortcuts import render
#method view
from django.core.exceptions import ObjectDoesNotExist
from input_data.models import PenjualanModel
from django.contrib.auth.decorators import login_required
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
            y = a + (b * (hitung_x ))
            # print((hitung_x + x_y))
            # print(hitung_x + x_y)
            y = round(y * index_musim_satuan[xzz])
            # print(index_musim_satuan[xzz])
            xzz+=1
            
            semua_data.append(y)
        x_y = 0
        semua_semua_data.append(sum(semua_data))
    return(semua_semua_data)
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
    jumlah_hotel_all = []
    jumlah_mall_all = []
    jumlah_apartemen_all = []
    jumlah_c441_all = []
    jumlah_c442_all = []
    jumlah_c443_all = []
    jumlah_c451_all = []
    jumlah_c452_all = []
    jumlah_c453_all = []
    jumlah_c461_all = []
    jumlah_c462_all = []
    jumlah_c463_all = []
    jasa_pembersih_air_all = []
    jasa_pembersih_kerak_sillica_all = []
    jasa_pembersih_cooling_tower_all = []
    jasa_pembersih_stp_all = []
    jumlah_asam_sulfat_all = []
    jumlah_molases_all = []
    jumlah_hcl_all = []
    jumlah_abf_all = []
    pendapatan_all = []
    jumlah_hotel_prediksi = []
    jumlah_mall_prediksi = []
    jumlah_apartemen_prediksi = []
    jumlah_c441_prediksi = []
    jumlah_c442_prediksi = []
    jumlah_c443_prediksi = []
    jumlah_c451_prediksi = []
    jumlah_c452_prediksi = []
    jumlah_c453_prediksi = []
    jumlah_c461_prediksi = []
    jumlah_c462_prediksi = []
    jumlah_c463_prediksi = []
    jasa_pembersih_air_prediksi = []
    jasa_pembersih_kerak_sillica_prediksi = []
    jasa_pembersih_cooling_tower_prediksi = []
    jasa_pembersih_stp_prediksi = []
    jumlah_asam_sulfat_prediksi = []
    jumlah_molases_prediksi = []
    jumlah_hcl_prediksi = []
    jumlah_abf_prediksi = []
    pendapatan_prediksi = []
    labeling = ""
    hitung = 0
    try:
        years= PenjualanModel.objects.all().order_by('tahun_transaksi')
        post_tahun = PenjualanModel.objects.values_list('tahun_transaksi', flat=True).order_by('tahun_transaksi').distinct()
        tahun = list(post_tahun)
        year_int = years[len(years) - 1].tahun_transaksi
        labeling="Pendapatan di Tahun " + str(year_int)
        x = 0
        tahunawal = tahun[0]
        hitungbulan = tahun[x]
        tahunsekarang = 0
    except ObjectDoesNotExist:
        year_int = 0
    
    try:
        for posts in years:
            hitung+=1
            tahunsekarang = posts.tahun_transaksi
            if tahunsekarang != hitungbulan:
                index_tahun = ((int(tahunsekarang) - tahunawal - 1) * 12)
                hasilprediksi = hitung_forecasting_tahun(years, index_tahun)
                jumlah_hotel_prediksi.append(hasilprediksi[0])
                jumlah_mall_prediksi.append(hasilprediksi[1])
                jumlah_apartemen_prediksi.append(hasilprediksi[2])
                jumlah_c441_prediksi.append(hasilprediksi[3])
                jumlah_c442_prediksi.append(hasilprediksi[4])
                jumlah_c443_prediksi.append(hasilprediksi[5])
                jumlah_c451_prediksi.append(hasilprediksi[6])
                jumlah_c452_prediksi.append(hasilprediksi[7])
                jumlah_c453_prediksi.append(hasilprediksi[8])
                jumlah_c461_prediksi.append(hasilprediksi[9])
                jumlah_c462_prediksi.append(hasilprediksi[10])
                jumlah_c463_prediksi.append(hasilprediksi[11])
                jasa_pembersih_air_prediksi.append(hasilprediksi[12])
                jasa_pembersih_kerak_sillica_prediksi.append(hasilprediksi[13])
                jasa_pembersih_cooling_tower_prediksi.append(hasilprediksi[14])
                jasa_pembersih_stp_prediksi.append(hasilprediksi[15])
                jumlah_asam_sulfat_prediksi.append(hasilprediksi[16])
                jumlah_molases_prediksi.append(hasilprediksi[17])
                jumlah_hcl_prediksi.append(hasilprediksi[18])
                jumlah_abf_prediksi.append(hasilprediksi[19])
                pendapatan_prediksi.append(hasilprediksi[20])
                hitung = 0
                x+= 1
                hitungbulan = tahun[x]
                jumlah_hotel_all.append(sum(jumlah_hotel))
                jumlah_mall_all.append(sum(jumlah_mall))
                jumlah_apartemen_all.append(sum(jumlah_apartemen))
                jumlah_c441_all.append(sum(jumlah_c441))
                jumlah_c442_all.append(sum(jumlah_c442))
                jumlah_c443_all.append(sum(jumlah_c443))
                jumlah_c451_all.append(sum(jumlah_c451))
                jumlah_c452_all.append(sum(jumlah_c452))
                jumlah_c453_all.append(sum(jumlah_c453))
                jumlah_c461_all.append(sum(jumlah_c461))
                jumlah_c462_all.append(sum(jumlah_c462))
                jumlah_c463_all.append(sum(jumlah_c463))
                jasa_pembersih_air_all.append(sum(jasa_pembersih_air))
                jasa_pembersih_kerak_sillica_all.append(sum(jasa_pembersih_kerak_sillica))
                jasa_pembersih_cooling_tower_all.append(sum(jasa_pembersih_cooling_tower))
                jasa_pembersih_stp_all.append(sum(jasa_pembersih_stp))
                jumlah_asam_sulfat_all.append(sum(jumlah_asam_sulfat))
                jumlah_molases_all.append(sum(jumlah_molases))
                jumlah_hcl_all.append(sum(jumlah_hcl))
                jumlah_abf_all.append(sum(jumlah_abf))
                pendapatan_all.append(sum(pendapatan))
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
        jumlah_hotel_all.append(sum(jumlah_hotel))
        jumlah_mall_all.append(sum(jumlah_mall))
        jumlah_apartemen_all.append(sum(jumlah_apartemen))
        jumlah_c441_all.append(sum(jumlah_c441))
        jumlah_c442_all.append(sum(jumlah_c442))
        jumlah_c443_all.append(sum(jumlah_c443))
        jumlah_c451_all.append(sum(jumlah_c451))
        jumlah_c452_all.append(sum(jumlah_c452))
        jumlah_c453_all.append(sum(jumlah_c453))
        jumlah_c461_all.append(sum(jumlah_c461))
        jumlah_c462_all.append(sum(jumlah_c462))
        jumlah_c463_all.append(sum(jumlah_c463))
        jasa_pembersih_air_all.append(sum(jasa_pembersih_air))
        jasa_pembersih_kerak_sillica_all.append(sum(jasa_pembersih_kerak_sillica))
        jasa_pembersih_cooling_tower_all.append(sum(jasa_pembersih_cooling_tower))
        jasa_pembersih_stp_all.append(sum(jasa_pembersih_stp))
        jumlah_asam_sulfat_all.append(sum(jumlah_asam_sulfat))
        jumlah_molases_all.append(sum(jumlah_molases))
        jumlah_hcl_all.append(sum(jumlah_hcl))
        jumlah_abf_all.append(sum(jumlah_abf))
        pendapatan_all.append(sum(pendapatan))
        jumlah_hotel_prediksi.append(hasilprediksi[0])
        jumlah_mall_prediksi.append(hasilprediksi[1])
        jumlah_apartemen_prediksi.append(hasilprediksi[2])
        jumlah_c441_prediksi.append(hasilprediksi[3])
        jumlah_c442_prediksi.append(hasilprediksi[4])
        jumlah_c443_prediksi.append(hasilprediksi[5])
        jumlah_c451_prediksi.append(hasilprediksi[6])
        jumlah_c452_prediksi.append(hasilprediksi[7])
        jumlah_c453_prediksi.append(hasilprediksi[8])
        jumlah_c461_prediksi.append(hasilprediksi[9])
        jumlah_c462_prediksi.append(hasilprediksi[10])
        jumlah_c463_prediksi.append(hasilprediksi[11])
        jasa_pembersih_air_prediksi.append(hasilprediksi[12])
        jasa_pembersih_kerak_sillica_prediksi.append(hasilprediksi[13])
        jasa_pembersih_cooling_tower_prediksi.append(hasilprediksi[14])
        jasa_pembersih_stp_prediksi.append(hasilprediksi[15])
        jumlah_asam_sulfat_prediksi.append(hasilprediksi[16])
        jumlah_molases_prediksi.append(hasilprediksi[17])
        jumlah_hcl_prediksi.append(hasilprediksi[18])
        jumlah_abf_prediksi.append(hasilprediksi[19])
        pendapatan_prediksi.append(hasilprediksi[20])
    except ObjectDoesNotExist:
        print("")


    
    context = {
        'title' : 'Home',
        'jumlah_hotel':  jumlah_hotel_all,
        'jumlah_mall': jumlah_mall_all,
        'jumlah_apartemen': jumlah_apartemen_all,
        'jumlah_c441': jumlah_c441_all,
        'jumlah_c442': jumlah_c442_all,
        'jumlah_c443': jumlah_c443_all,
        'jumlah_c451': jumlah_c451_all,
        'jumlah_c452': jumlah_c452_all,
        'jumlah_c453': jumlah_c453_all,
        'jumlah_c461': jumlah_c461_all,
        'jumlah_c462': jumlah_c462_all,
        'jumlah_c463': jumlah_c463_all,
        'jasa_pembersih_air': jasa_pembersih_air_all,
        'jasa_pembersih_kerak_sillica': jasa_pembersih_kerak_sillica_all, 
        'jasa_pembersih_cooling_tower': jasa_pembersih_cooling_tower_all, 
        'jasa_pembersih_stp': jasa_pembersih_stp_all,
        'jumlah_asam_sulfat': jumlah_asam_sulfat_all,
        'jumlah_molases': jumlah_molases_all,
        'jumlah_hcl': jumlah_hcl_all,
        'jumlah_abf': jumlah_abf_all,
        'pendapatan':  pendapatan_all,
        'labeling': labeling,
        'tahun': tahun,
        'jumlah_hotel_prediksi':  jumlah_hotel_prediksi,
        'jumlah_mall_prediksi':        jumlah_mall_prediksi,
        'jumlah_apartemen_prediksi':        jumlah_apartemen_prediksi,
        'jumlah_c441_prediksi':        jumlah_c441_prediksi,
        'jumlah_c442_prediksi':        jumlah_c442_prediksi,
        'jumlah_c443_prediksi':        jumlah_c443_prediksi,
        'jumlah_c451_prediksi':        jumlah_c451_prediksi,
        'jumlah_c452_prediksi':        jumlah_c452_prediksi,
        'jumlah_c453_prediksi':        jumlah_c453_prediksi,
        'jumlah_c461_prediksi':        jumlah_c461_prediksi,
        'jumlah_c462_prediksi':        jumlah_c462_prediksi,
        'jumlah_c463_prediksi':        jumlah_c463_prediksi,
        'jasa_pembersih_air_prediksi':        jasa_pembersih_air_prediksi,
        'jasa_pembersih_kerak_sillica_prediksi' :        jasa_pembersih_kerak_sillica_prediksi,
        'jasa_pembersih_cooling_tower_prediksi':        jasa_pembersih_cooling_tower_prediksi,
        'jasa_pembersih_stp_prediksi':        jasa_pembersih_stp_prediksi,
        'jumlah_asam_sulfat_prediksi':        jumlah_asam_sulfat_prediksi,
        'jumlah_molases_prediksi':        jumlah_molases_prediksi,
        'jumlah_hcl_prediksi':        jumlah_hcl_prediksi,
        'jumlah_abf_prediksi':        jumlah_abf_prediksi,
        'pendapatan_prediksi':        pendapatan_prediksi,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
