from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Waleed',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2028'
    },
    {
        'author': 'Ouiji',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2028'
    }
]


def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})