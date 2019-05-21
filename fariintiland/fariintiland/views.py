# from django.http import HttpResponse
from django.shortcuts import render
#method view

def index(request):
    context = {
        'title' : 'Home',
        'heading' : 'Yutrif',
        'subheading' : 'yudha',
        'banner' : 'img/banner_home.png',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ]
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
