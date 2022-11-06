from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def index(requset):
    return render(requset, 'blog/post/index.html')

def post_list(requset):
    posts = Post.objects.filter(status="published")
    paginator = Paginator(posts,8)
    page = requset.GET.get('page')

    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)
    return render(requset,'blog/post/list.html',{'posts':posts,'page':page})

def post_detail(requset,post,pk):
    post = get_object_or_404(Post,slug=post,id=pk)
    return render(requset,'blog/post/detail.html',{"post":post})