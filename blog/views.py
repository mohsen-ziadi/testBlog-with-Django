from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Post,Account
from .forms import AccountForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.views.generic import ListView
def index(requset):
    return render(requset, 'blog/post/index.html')

# def post_list(requset):
#     posts = Post.objects.filter(status="published")
#     paginator = Paginator(posts,8)
#     page = requset.GET.get('page')
#
#     try:
#         posts=paginator.page(page)
#     except PageNotAnInteger:
#         posts=paginator.page(1)
#     except EmptyPage:
#         posts=paginator.page(paginator.num_pages)
#     return render(requset,'blog/post/list.html',{'posts':posts,'page':page})

class PostListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = 'posts'
    paginate_by = 8
    template_name = 'blog/post/list.html'

def post_detail(requset,post,pk):
    post = get_object_or_404(Post,slug=post,id=pk)
    return render(requset,'blog/post/detail.html',{"post":post})

def UserAcconut(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountForm()
    return render(request,"blog/forms/account_form.html",{'form':form})
