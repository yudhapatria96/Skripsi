from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.

def index(request):

    posts = Post.objects.all() 
    context = {
        'title' : 'Blog',
        'heading': 'Blog',
        'posts' : posts,
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

def berita(request):

    posts = Post.objects.filter(category__iexact='berita')
    context = {
        'title' : 'Blog',
        'heading': 'Blog',
        'posts' : posts,
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

def jurnal(request):

    posts = Post.objects.filter(category__iexact='jurnal')
    context = {
        'title' : 'Blog',
        'heading': 'Blog',
        'posts' : posts,
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

def angka(request, angka):

    posts = Post.objects.filter(id__iexact=angka)
    context = {
        'title' : 'Blog',
        'heading': 'Blog',
        'posts' : posts,
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