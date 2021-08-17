from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
posts = [
    {
        'author': 'Zhanghang',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'data_posted':'August 28, 2018'
    },
    {
        'author': 'John',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'data_posted':'August 29, 2018'
    }, 
]

def home(request):

    context = {
        'posts': Post.objects.all(),
        'title': 'blog-home'
    }
    return render(request, 'blog/home.html' ,context)
    #return HttpResponse('')

def about(request):
    return render(request, 'blog/about.html' )
    #return HttpResponse('')
    return HttpResponse('')

