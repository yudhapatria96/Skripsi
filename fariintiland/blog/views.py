from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.

def index(request):

    posts = Post.objects.all() 
    categories = Post.objects.values('category').distinct()

    context = {
        'title' : 'Blog',
        'heading': 'Blog',
        'posts' : posts,
        'categories': categories,
        'content' : 'Ini adalah blog',
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


def category(request, category):

    posts = Post.objects.filter(category=category)
    categories = Post.objects.values('category').distinct()
    context = {
        'title' : 'Category',
        'heading': 'Category',
        'content' : 'tampilkan berdasarkan category',
        'posts' : posts,
        'subheading': 'Jurnal Kelas Terbuka',
        'kontributor' : 'yudha',
        'categories' : categories,
        'banner' : 'blog/img/banner_blog.png',
        'app_css' : 'blog/css/styles.css',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ]
    }
    return render(request, 'blog/category.html', context)

def singlePost(request, slug):

    posts = Post.objects.get(slug=slug)
    categories = Post.objects.values('category').distinct()
    context = {
        'title' : 'Blog',
        'heading': 'Blog',
        'posts' : posts,
        'categories': categories,
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
    return render(request,'blog/detail.html', context)