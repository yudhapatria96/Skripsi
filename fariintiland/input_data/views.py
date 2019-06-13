from django.shortcuts import render, redirect

# Create your views here.
from . import forms
from . import models
def index(request):
    post = models.PenjualanModel.objects.all()
    contact_form = forms.ContactForm()
    for postss in post:
        print(postss)
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