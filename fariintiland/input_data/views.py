from django.shortcuts import render, redirect
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
# Create your views here.
from . import forms
from . import models
from django.db import IntegrityError
def index(request):
    post = models.PenjualanModel.objects.all()
    contact_form = forms.ContactForm()
    # for posts in post:
    #     print(posts.bulan_transaksi)
    context = {
        'heading':'Contact',
        'data_form':contact_form,
        'posts' : post,

    }

    return render(request, 'inputdata/index.html',context)

def create(request):
    contact_form = forms.ContactForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()


        return redirect('input_data:index')
        # models.PenjualanModel.objects.create(
        #     bulan_transaksi = request.POST['tanggal_field_month'],
        #     tahun_transaksi = request.POST['tanggal_field_year'],
        #     jumlah_hotel = request.POST['hotel_field'],
        #     jumlah_mall = request.POST['mall_field'],
        #     jumlah_apartemen= request.POST['apartement_field'],
        #     jumlah_C441= request.POST['c441_field'],
        #     jumlah_C442= request.POST['c442_field'],
        #     jumlah_C443= request.POST['c443_field'],
        #     jumlah_C451= request.POST['c451_field'],
        #     jumlah_C452= request.POST['c452_field'],
        #     jumlah_C453= request.POST['c453_field'],
        #     jumlah_C461= request.POST['c461_field'],
        #     jumlah_C462= request.POST['c462_field'],
        #     jumlah_C463= request.POST['c463_field'],
        #     jasa_pembersih_air= request.POST['pembersih_air_field'],
        #     jasa_pembersih_kerak_sillica = request.POST['pembersih_kerak_field'],
        #     jasa_pembersih_cooling_tower = request.POST['pembesih_cooling_tower_field'],
        #     jasa_pembersih_stp = request.POST['pembersih_stp_field'],
        #     jumlah_asam_sulfat =  request.POST['asam_sulfat_field'],
        #     jumlah_molases = request.POST['molases_field'],
        #     jumlah_hcl = request.POST['hcl_field'],
        #     jumlah_abf = request.POST['abf_field'],
        # )
    context = {
        'heading':'Contact',
        'contact_form':contact_form,

    }

    return render(request, 'inputdata/input.html',context)

def delete(request, delete_id):
    models.PenjualanModel.objects.filter(id_penjualan=delete_id).delete()
    return redirect('input_data:index')

def update(request, update_id):
    penjualan = models.PenjualanModel.objects.get(id_penjualan=update_id)

    penjualan_form = forms.ContactForm(request.POST or None, instance=penjualan)
    
    context = {
        'heading':'Update',
        'contact_form':penjualan_form,

    }
    if request.method == 'POST':
        if penjualan_form.is_valid():

           penjualan_form.save()

        return redirect('input_data:index')
    return render(request, 'inputdata/input.html', context)

# @permission_required('admin.can_add_log_entry')
def inputcsv(request):
  
    prompt = {
        'order': 'Urutan data pada CSV yaitu id_penjualan, bulan_transaksi, tahun_transaksi, jumlah_hotel, jumlah_mall, jumlah_apartemen, jumlah_c441, jumlahc442, jumlah_c443, jumlah_c451, jumlahc452, jumlahc453, jumlahc461, jumlahc462, jumlahc463, jasa_pembersih_air, jasa_pembersih_kerak_silica, jasa_pembersih_cooling_tower, jasa_pembersih_stp, jumlah_asam_sulfat, jumlah_molases, jumlah_hcl, jumlah_abf, pendapatan',
        'order2': 'Apabila menggunakan Excel, gunakan format save .CSV(Comma delimited)'
    }
    
    if request.method == "GET":
         return render(request, 'inputdata/inputcsv.html', prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "Bukan Format .csv")
    else:
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            #  if models.PenjualanModel.objects.filter(id_penjualan=column[0]):
            #     continue
            #  else:
            # for tesst in len(column):
            #     if column[tesst] == None:
           
            try:
                if models.PenjualanModel.objects.filter(bulan_transaksi = column[1], tahun_transaksi = column[2]):
                   
                    models.PenjualanModel.objects.filter(bulan_transaksi = column[1], tahun_transaksi = column[2]).update( bulan_transaksi = column[1],
                    tahun_transaksi = column[2],
                    jumlah_hotel = column[3],
                    jumlah_mall = column[4],
                    jumlah_apartemen= column[5],
                    jumlah_C441= column[6],
                    jumlah_C442= column[7],
                    jumlah_C443= column[8],
                    jumlah_C451= column[9],
                    jumlah_C452= column[10],
                    jumlah_C453= column[11],
                    jumlah_C461= column[12],
                    jumlah_C462= column[13],
                    jumlah_C463= column[14],
                    jasa_pembersih_air= column[15],
                    jasa_pembersih_kerak_sillica = column[16],
                    jasa_pembersih_cooling_tower = column[17],
                    jasa_pembersih_stp = column[18],
                    jumlah_asam_sulfat =  column[19],
                    jumlah_molases = column[20],
                    jumlah_hcl = column[21],
                    jumlah_abf = column[22],
                    pendapatan = column[23] )
                    messages.success(request, "Pada bulan "+ column[1] + " tahun "+ column[2]+" data berhasil di update")
                else:
                    try:   
                        _, created = models.PenjualanModel.objects.update_or_create(
                        id_penjualan = column[0],
                        bulan_transaksi = column[1],
                        tahun_transaksi = column[2],
                        jumlah_hotel = column[3],
                        jumlah_mall = column[4],
                        jumlah_apartemen= column[5],
                        jumlah_C441= column[6],
                        jumlah_C442= column[7],
                        jumlah_C443= column[8],
                        jumlah_C451= column[9],
                        jumlah_C452= column[10],
                        jumlah_C453= column[11],
                        jumlah_C461= column[12],
                        jumlah_C462= column[13],
                        jumlah_C463= column[14],
                        jasa_pembersih_air= column[15],
                        jasa_pembersih_kerak_sillica = column[16],
                        jasa_pembersih_cooling_tower = column[17],
                        jasa_pembersih_stp = column[18],
                        jumlah_asam_sulfat =  column[19],
                        jumlah_molases = column[20],
                        jumlah_hcl = column[21],
                        jumlah_abf = column[22],   
                        pendapatan = column[23] 
                    )
                        messages.success(request, "Pada bulan "+ column[1] + " tahun "+ column[2]+" data berhasil di masukkan ke database")
                    except IntegrityError:
                        models.PenjualanModel.objects.filter(id_penjualan = column[0]).update( bulan_transaksi = column[1],
                        tahun_transaksi = column[2],
                        jumlah_hotel = column[3],
                        jumlah_mall = column[4],
                        jumlah_apartemen= column[5],
                        jumlah_C441= column[6],
                        jumlah_C442= column[7],
                        jumlah_C443= column[8],
                        jumlah_C451= column[9],
                        jumlah_C452= column[10],
                        jumlah_C453= column[11],
                        jumlah_C461= column[12],
                        jumlah_C462= column[13],
                        jumlah_C463= column[14],
                        jasa_pembersih_air= column[15],
                        jasa_pembersih_kerak_sillica = column[16],
                        jasa_pembersih_cooling_tower = column[17],
                        jasa_pembersih_stp = column[18],
                        jumlah_asam_sulfat =  column[19],
                        jumlah_molases = column[20],
                        jumlah_hcl = column[21],
                        jumlah_abf = column[22],
                        pendapatan = column[23] )
                        messages.success(request, "Pada bulan "+ column[1] + " tahun "+ column[2]+" data berhasil di update")
                    except ValueError:

                        messages.error(request, "Terdapat data kosong di bulan  "+ column[1] + " tahun "+ column[2]+" . Data tidak dimasukkan ke database")
                        break
                
            except ValueError:
                messages.error(request, "Terdapat data kosong di bulan  "+ column[1] + " tahun "+ column[2]+" . Data tidak dimasukkan ke database")
                break
            

    context = {

    }
    return render(request, 'inputdata/inputcsv.html',context)