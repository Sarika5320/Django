from django.shortcuts import render,redirect,HttpResponse
from .models import Blog,Comment,Replay
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.urls import reverse


# Create your views here.

def home(request):

  blog = Blog.objects.all()

  context ={
    "blog":blog
  }

  return render(request,"home.html",context)

def about(request):
  return render(request,"about.html")

def contact(request):
  return render(request,"contact.html")


def content(request,id):
  comment = Comment.objects.all().order_by('-id')
  blog = Blog.objects.get(id=id)
  replay = Replay.objects.all()
  context = {
    "blog": blog,
    "comment":comment,
    "replay":replay
  }
  return render(request,"blogcontent.html",context)

def signup(request): 
  if request.method=="POST":
    fname = request.POST.get("fname")
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = User.objects.create_user (first_name=fname,username=email,email=email,password=password)
    user.save()
    messages.success(request, "Congratulations! Your signup was successful. Let’s get started!")
    return redirect("home")
  return render(request,"signup.html")

def Login(request):
  if request.method=="POST":
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = authenticate(request,username=email, password=password)

    if user is not None:
      messages.success(request, "You have successfully logged in.")
      login(request,user) 
    else:
      messages.error(request, "Invalid Credentials.")
    return redirect("home")
  return render(request,"login.html")

def Logout(request):
  logout(request)
  return redirect("home")


def comment(request):
  if request.method == "POST":
    name = request.user
    blog_id = request.POST.get("blogid")
    comment = request.POST.get("comment")

    blog = Blog.objects.get(id=blog_id)
    comment =Comment(name=name,blogparent=blog,comment=comment)

    comment.save()
    messages.success(request,"Your comment successfully added!")
    
  return redirect(reverse("content", args=[blog_id])) 



def replies(request):
  if request.method=="POST":
    name = request.user
    commentparent = request.POST.get("commentparent")
    replay = request.POST.get("replay")
    blog_id = request.POST.get("blogid")

    comment = Comment.objects.get(id=commentparent)

    replied = Replay(name=name,commentparent=comment,replay=replay)
    replied.save()
    messages.success(request,"Your replay successfully added!")
  return redirect(reverse("content", args=[blog_id]))