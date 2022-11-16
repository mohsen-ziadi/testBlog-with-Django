from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.core.mail import send_mail
from django.views.generic import ListView
from django.contrib.auth import login,authenticate,logout

# Create your views here.
from .models import Post,Account
from  .forms import *

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


#functions
def post_detail(requset,post,pk):
    post = get_object_or_404(Post,slug=post,id=pk)
    sent = False
    form = ShareForm(requset.POST)
    if requset.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            post_url = requset.build_absolute_uri()
            subject = ".{0} شما را به خواندن متن {1} دعوت کرده است.".format(cd['name_share'],post.title)
            msg='با سلام .{0} .{1} شما را به خواندن متن {2} دعوت کرده است. {3} با تشکر {4} بلاگ نمونه'.format('\n', cd['name_share'],post.title,'\n','\n ')
            send_mail(subject,msg,'mohzia1380@gmail.com',[cd['email_share']],fail_silently=False)
            sent=True
            return render(requset,'blog/post/detail.html',{"post":post,'form':form})
        else:
            form=ShareForm()
            return render(requset, 'blog/post/detail.html', {"post": post, 'form': form})
    return render(requset,'blog/post/detail.html',{"post":post,'form':form})


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
            account.phone = form.cleaned_data['phone']
            account.address = form.cleaned_data['address']
            user.save()
            account.save()
            return redirect('index')
        else:
            return render(request,'blog/forms/account_form.html',{'form':form,'account':account})
    form = AccountForm()
    return render(request,'blog/forms/account_form.html',{'form':form,'account':account})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blog:UserAccount')
                else:
                    return redirect('blog:index')
            else:
                return redirect('blog:index')
    else:
        form = LoginForm()
    return render(request,'blog/forms/login.html',{"form":form})

def loguot_view(request):
    logout(request)
    return redirect("login")






