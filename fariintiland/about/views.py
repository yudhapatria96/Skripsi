from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
       'title' : 'About',
        'heading': 'About',
        'subheading': 'tentang kelas terbuka',
        'banner' : 'about/img/banner_about.png',
        'app_css' : 'about/css/styles.css',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ]
    }
    return render(request, 'about/index.html', context)