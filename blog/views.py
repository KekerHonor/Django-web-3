from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

def post(request):
    posts = Post.objects.all()
    data = {
        "posts" : posts
    }
    return render(request, "post.html", data)
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")