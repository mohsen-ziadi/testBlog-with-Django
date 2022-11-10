from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import send_mail
from django.views.generic import ListView

# Create your views here.
from .models import Post,Account
from  .forms import AccountForm

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


def UserAccount(request):
    user =request.user
    try:
        account =Account.objects.get(user = user)

    except:
        account = Account.objects.create(user=user)

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            account.gender = form.cleaned_data['gender']
            account.address = form.cleaned_data['address']
            user.save()
            account.save()
            return redirect('index')
        else:
            return render(request,'blog/forms/account_form.html',{'form':form,'account':account})
    form = AccountForm()
    return render(request,'blog/forms/account_form.html',{'form':form,'account':account})



