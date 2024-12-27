from django.shortcuts import render
from .models import *

# Create your views here.

#view for register page
def RegisterPage(request):
 return render(request,"app/register.html")

#view for user registration
def UserRegister(request):
 if request.method=="POST":
  fname=request.POST['fname']
  lname=request.POST['lname']
  email=request.POST['email']
  contact=request.POST['contact']
  password=request.POST['password']
  cpassword=request.POST['cpassword']
  #first we will validate that the user already exist
  user=User.objects.filter(Email=email)
  if user:
   message="user already exist"
   return render(request,"app/register.html",{'msg':message})
  else:
   if password==cpassword:
    newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,
                                Contact=contact,Password=password)
    message="User register successfully"
    return render(request,"app/login.html",{'msg':message})
   else:
    message="Password and ConformPassword does not match"
    return render(request,"app/register.html",{'msg':message})