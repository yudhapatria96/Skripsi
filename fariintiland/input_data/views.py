from django.shortcuts import render

# Create your views here.
from . import forms

def index(request):
    contact_form = forms.ContactForm()
    context = {
        'heading':'Contact',
        'data_form':contact_form,

    }

    return render(request, 'inputdata/index.html',context)