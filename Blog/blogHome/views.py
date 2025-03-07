from django.shortcuts import render,redirect,HttpResponse
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages


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
  blog = Blog.objects.get(id=id)
  context = {
    "blog": blog
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