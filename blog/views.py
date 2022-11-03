from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(requset):
    return HttpResponse("Hello World")

def post_list(requset):
    posts = Post.objects.filter(status="published")
    return render(requset,'blog/post/list.html',{'posts':posts})

def post_detail(requset):
    return render(requset,'blog/post/detail.html')