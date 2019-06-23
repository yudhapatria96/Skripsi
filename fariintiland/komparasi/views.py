from django.shortcuts import render
from input_data.models import PenjualanModel


def index(request):

    post_tahun = PenjualanModel.objects.values_list('tahun_transaksi', flat=True).distinct()

    
    context = {
        'heading':'Forecasting',
        'tahun': post_tahun,
        
    } 
  
                
    return render(request, 'komparasi/index.html',context)
