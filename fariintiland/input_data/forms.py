from django import forms

class ContactForm(forms.Form):
    e301_field = forms.IntegerField(
        label = "Jumlah E301", 
        widget = forms.TextInput(
              attrs={
                  'class': 'form-control',
                  'placeholder': 'masukan jumlah penjualan E301'
              }
            )
        )
    e302_field = forms.IntegerField(label="Jumlah E302")
    e303_field = forms.IntegerField(label="Jumlah E303")
    e101_field = forms.IntegerField(label="Jumlah E101")
    e102_field = forms.IntegerField(label="Jumlah E102")
    e103_field = forms.IntegerField(label="Jumlah E103")
    e201_field = forms.IntegerField(label="Jumlah E201")
    e202_field = forms.IntegerField(label="Jumlah E202")
    e203_field = forms.IntegerField(label="Jumlah E203")
