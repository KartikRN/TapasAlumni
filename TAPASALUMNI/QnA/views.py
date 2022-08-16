from django.shortcuts import render,HttpResponse,redirect
from .models import post
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from .forms import PostForm

# Create your views here.
def QnA(request):
    Post = post.objects.all()
    return HttpResponse("this is Qna")

def editor(request,id):
    Post = post.objects.filter(post_id=id)[0]
    if request.method == "POST":
        title = request.POST.get("title")
        form = PostForm(instance=Post, data=request.POST)
        if form.is_valid():
            post_item=form.save(commit=False)
            post_item.title=title
            post_item.pub_date=datetime.datetime.now()
            if request.FILES.get("banner"):
                image = request.FILES.get("banner")
                post_item.Banner_image=image
            post_item.save()
            return redirect("/blogs/dashboard")
    else:
        form = PostForm(instance=Post)
    return render(request, 'blog/editor.html',{"post":Post,"form":form})


def write(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST.get("title")
            image = request.FILES.get("banner")
            form=PostForm(request.POST)
            if form.is_valid():
                post_item=form.save(commit=False)
                post_item.user=request.user
                post_item.title=title
                post_item.pub_date=datetime.datetime.now()
                post_item.Banner_image=image
                post_item.save()
            return redirect("/blogs")
        else:
            form = PostForm()
        return render(request, 'blog/write.html',{'form':form})
    else:
        messages.error(request, "Login to continue")
        return redirect("/account/login")

def post(request, id):
    Post = post.objects.filter(post_id=id)[0]
    try:
        more = post.objects.filter(post_id=id+1)[0]
        return render(request, 'blog/blog.html', {'post': Post, 'more': more})
    except IndexError:
        return render(request, 'blog/blog.html', {'post': Post})



def dashboard(request):
    if request.user.is_authenticated:
        Post = post.objects.filter(user=request.user)
        return render(request, 'blog/dashboard.html',{"post":Post})
    else:
        return HttpResponse("404-page not found")


def delete(request,id):
    Post = post.objects.filter(post_id=id)[0]
    Post.delete()
    return redirect("/blogs/dashboard")