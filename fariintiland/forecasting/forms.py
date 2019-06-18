from django import forms
from . import widgets


class DatingForm(forms.Form):
    bulan_dan_tahun_prediksi = forms.CharField(widget=widgets.MonthYearWidget(attrs={"class": "select"}))
    
    class Meta:
        fields = ('__all__')