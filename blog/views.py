from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requset):
    return HttpResponse("Hello World")

def post_list(requset):
    return render(requset,'blog/post/list.html')

def post_detail(requset):
    return render(requset,'blog/post/detail.html')