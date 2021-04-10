from django.shortcuts import render
from . models import Post

# Create your views here.
def showblog(requests):
    posts = Post.objects
    return render(requests, 'blog/blog.html', {'posts': posts})
