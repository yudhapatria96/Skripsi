from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'title' : 'Blog',
        'heading': 'Blog',
        'subheading': 'Jurnal Kelas Terbuka',
        'kontributor' : 'yudha',
        'banner' : 'blog/img/banner_blog.png',
        'app_css' : 'blog/css/styles.css',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ]
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul' : 'News',
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul' : 'Cerita',
    }
    return render(request, 'blog/index.html', context)