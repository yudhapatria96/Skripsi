from django import forms

class ContactForm(forms.Form):
  
    TAHUN= range(2000, 2050, 1)
    tanggal_field = forms.DateField(
        label = "Tanggal_Transaksi",
        widget = forms.SelectDateWidget(years=TAHUN)
    )
    hotel_field         = forms.IntegerField(
        label="Jumlah Hotel",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah client hotel'
              }
            ))
    mall_field          = forms.IntegerField(
        label="Jumlah Mall",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah client mall'
              }
            ))
    apartement_field    = forms.IntegerField(
        label="Jumlah apartement",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah client apartement'
              }
            ))
    c441_field          = forms.IntegerField(
        label="Jumlah C441",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah C441'
              }
            ))
    c442_field          = forms.IntegerField(
        label="Jumlah C442",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan C442'
              }
            ))
    c443_field          = forms.IntegerField(
        label="Jumlah C443",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan C443'
              }
            ))
    c451_field          = forms.IntegerField(
        label="Jumlah C451",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan C451'
              }
            ))
    c452_field          = forms.IntegerField(
        label="Jumlah C452",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan C452'
              }
            ))
    c453_field          = forms.IntegerField(
        label="Jumlah C453",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan C453'
              }
            ))
    c461_field          = forms.IntegerField(
        label = "Jumlah C461", 
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan C461'
              }
            )
    )    
    c462_field                   = forms.IntegerField(
        label="Jumlah C462",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan C462'
              }
            ))
    c463_field                   = forms.IntegerField(
        label="Jumlah C463",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan E463'
              }
            ))
    pembersih_air_field          = forms.IntegerField(
        label="Jumlah Jasa Pembersih Air",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah jasa pembersih air'
              }
            ))
    pembersih_kerak_field        = forms.IntegerField(
        label="Jumlah Jasa Pembersih Kerak Sillica",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah jasa pembersih kerak sillica'
              }
            ))
    pembesih_cooling_tower_field = forms.IntegerField(
        label="Jumlah Jasa Pembersih Cooling Tower",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah pembersih cooling tower'
              }
            ))
    pembersih_stp_field          = forms.IntegerField(
        label="Jumlah Jasa Pembersih STP",
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah jasa pembersih STP'
              }
            ))

   
    
