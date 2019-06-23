from django import forms
from . import widgets
from input_data.models import PenjualanModel


class DatingForm(forms.Form):
    # MONTH_CHOICES= [
    # (1, "januari"),   
    # (2, "februari"),
    # (3, "maret"),
    # (4, "april"),
    # (5, "mei"),
    # (6, "juni"),
    # (7, "juli"),
    # (8, "agustus"),
    # (9, "september"),   
    # (10, "oktober"),
    # (11, "november"),    
    # (12, "desember")
    # ]
    # years= PenjualanModel.objects.all().order_by('tahun_transaksi')
    # year_int = years[len(years) - 1].tahun_transaksi


    # INTEGER_CHOICES= [tuple([x,x]) for x in range(year_int+1, year_int+10)]

    bulan_dan_tahun_prediksi = forms.CharField(widget=widgets.MonthYearWidget(attrs={"class": "select"}))
    # todays_date= forms.IntegerField(label="What is today's date?", widget=forms.Select(choices=INTEGER_CHOICES))
    # bulan_prediksi =  forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=MONTH_CHOICES))
    class Meta:
        fields = ('__all__')