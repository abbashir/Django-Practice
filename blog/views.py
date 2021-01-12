from django.shortcuts import render
from django.http import HttpResponse

# make dummy post data
posts = [
    {
        'author': 'abdul bashir',
        'title': 'blog post title 1',
        'content': 'blog post content 1',
        'date_posted': 'january 12, 2021'
    },
    {
        'author': 'harry',
        'title': 'blog post title 2',
        'content': 'blog post content 2',
        'date_posted': 'january 13, 2021',
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
