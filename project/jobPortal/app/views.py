from django.shortcuts import render
from .models import *
from random import randint

# Create your views here.


def IndexPage(request):
   return render(request, "app/index.html")


def SignupPage(request):
   return render(request, "app/signup.html")


def RegisterUser(request):
   if request.POST["role"] == "Candidate":
      role = request.POST["role"]
      fname = request.POST["firstname"]
      lname = request.POST["lastname"]
      email = request.POST["email"]
      password = request.POST["password"]
      cpassword=request.POST["cpassword"]

      # server-side validation
      user = UserMaster.objects.filter(email=email)
      if user:
         message = "User already exist"
         return render(request, "app/signup.html", {"msg": message})
      else:
         if password == cpassword:
            otp = randint(100000, 999999)
            newuser = UserMaster.objects.create(
               role=role, otp=otp, email=email, password=password
               )
            newcand = Candidate.objects.create(
               user_id=newuser, firstname=fname, lastname=lname
               )
            return render(request, "app/otpverify.html",{'email':email})
   else:
      print("Company registration")

def RegisterCompany(request):
   if request.POST["role"]=="Company":
      role=request.POST["role"]
      fname=request.POST["firstname"]
      lname = request.POST["lastname"]
      email = request.POST["email"]
      password = request.POST["password"]
      cpassword=request.POST["cpassword"]
      
      #server side validation
      user = UserMaster.objects.filter(email=email)
      if user:
         message = "Company already exist"
         return render(request, "app/signup.html", {"msg": message})
      else:
            if password == cpassword:
               otp = randint(100000, 999999)
               newuser = UserMaster.objects.create(
               role=role, otp=otp, email=email, password=password)
               newcomp = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
               return render(request, "app/otpverify.html",{'email':email})
            else:
               print("Candidate registration")
         
def OTPPage(request):
   return render(request,"app/otpverify.html")

def Otpverify(request):
   email=request.POST['email']
   otp=int(request.POST['otp'])
   
   user=UserMaster.objects.get(email=email)
   if user:
      if user.otp==otp:
         message="Otp Verification Successful"
         return render(request,"app/login.html", {'msg':message})
      else:
         message="Otp is incorrect"
         return render(request,"app/otpverify.html",{'msg':message})
   else:
      return render(request,"app/signup.html")