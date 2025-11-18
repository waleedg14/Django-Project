from django.shortcuts import render

posts =[
    {
        'author': 'Waleed',
        'title':'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2025'
    },
    {
            'author': 'Japreet',
        'title':'Blog post 2',
        'content': 'First post content',
        'date_posted': 'August 29, 2025'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


