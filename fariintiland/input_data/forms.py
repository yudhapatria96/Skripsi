from django import forms

from . import models
class ContactForm(forms.ModelForm):
  class Meta:
    model = models.PenjualanModel
    TAHUN= range(2000, 2050, 1)
    fields = [
'bulan_transaksi',        
'tahun_transaksi',
'jumlah_hotel',
'jumlah_mall',
'jumlah_apartemen',
'jumlah_C441',
'jumlah_C442',
'jumlah_C443',
'jumlah_C451',
'jumlah_C452',
'jumlah_C453',
'jumlah_C461',
'jumlah_C462',
'jumlah_C463',
'jasa_pembersih_air',
'jasa_pembersih_kerak_sillica',
'jasa_pembersih_cooling_tower',
'jasa_pembersih_stp',
'jumlah_asam_sulfat',
'jumlah_molases',
'jumlah_hcl',
'jumlah_abf',
    ]
#     widget ={
#     tanggal_field = forms.DateField(
#         label = "Tanggal_Transaksi",
#         widget = forms.SelectDateWidget(years=TAHUN)
#     )
#     hotel_field         = forms.IntegerField(
#         label="Jumlah Hotel",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah client hotel'
#               }
#             ))
#     mall_field          = forms.IntegerField(
#         label="Jumlah Mall",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah client mall'
#               }
#             ))
#     apartement_field    = forms.IntegerField(
#         label="Jumlah apartement",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah client apartement'
#               }
#             ))
#     c441_field          = forms.IntegerField(
#         label="Jumlah C441",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah C441'
#               }
#             ))
#     c442_field          = forms.IntegerField(
#         label="Jumlah C442",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah penjualan C442'
#               }
#             ))
#     c443_field          = forms.IntegerField(
#         label="Jumlah C443",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah penjualan C443'
#               }
#             ))
#     c451_field          = forms.IntegerField(
#         label="Jumlah C451",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah penjualan C451'
#               }
#             ))
#     c452_field          = forms.IntegerField(
#         label="Jumlah C452",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah penjualan C452'
#               }
#             ))
#     c453_field          = forms.IntegerField(
#         label="Jumlah C453",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah penjualan C453'
#               }
#             ))
#     c461_field          = forms.IntegerField(
#         label = "Jumlah C461", 
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah penjualan C461'
#               }
#             )
#     )    
#     c462_field                   = forms.IntegerField(
#         label="Jumlah C462",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah penjualan C462'
#               }
#             ))
#     c463_field                   = forms.IntegerField(
#         label="Jumlah C463",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah penjualan E463'
#               }
#             ))
#     pembersih_air_field          = forms.IntegerField(
#         label="Jumlah Jasa Pembersih Air",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah jasa pembersih air'
#               }
#             ))
#     pembersih_kerak_field        = forms.IntegerField(
#         label="Jumlah Jasa Pembersih Kerak Sillica",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah jasa pembersih kerak sillica'
#               }
#             ))
#     pembesih_cooling_tower_field = forms.IntegerField(
#         label="Jumlah Jasa Pembersih Cooling Tower",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah pembersih cooling tower'
#               }
#             ))
#     pembersih_stp_field          = forms.IntegerField(
#         label="Jumlah Jasa Pembersih STP",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah jasa pembersih STP'
#               }
#             ))
#     asam_sulfat_field          = forms.IntegerField(
#         label="Jumlah Asam Sulfat",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah asam sulfat terpakai'
#               }
#             ))   
#     molases_field          = forms.IntegerField(
#         label="Jumlah Molases",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah molases terpakai'
#               }
#             ))       
#     hcl_field          = forms.IntegerField(
#         label="Jumlah HCL",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah HCL terpakai'
#               }
#             ))
#     abf_field          = forms.IntegerField(
#         label="Jumlah ABF",
#         widget = forms.TextInput(
#               attrs={
#                   'class': 'form-control',
#                   'placeholder': 'masukan jumlah ABF terpakai'
#               }
#             )) 
#  }  
    
