from django.shortcuts import render,redirect
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
      if request.POST["role"]=="Company":
         role=request.POST['role']
         fname=request.POST['firstname']
         lname=request.POST['lastname']
         email=request.POST['email']
         password=request.POST['password']
         cpassword=request.POST['cpassword']
         
         user1=UserMaster.objects.filter(email=email)
         if user1:
            message="Company already exist"
            return render(request, "app/signup.html", {"msg":message})
         else:
            if password==cpassword:
               otp=randint(100000,999999)
               newuser1=UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
               newcomp=Company.objects.create(user_id=newuser1,firstname=fname,lastname=lname)
               return render(request, "app/otpverify.html",{'email':email})

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

def Loginpage(request):
   return render(request,"app/login.html")


def LoginUser(request):
   if request.method == "POST":
      # Validate 'role' key existence and non-empty value
      role = request.POST.get("role", None)
      if not role:
         message = "Please select a role."
         return render(request, "app/login.html", {"msg": message})

      email = request.POST.get("email")
      password = request.POST.get("password")

      try:
         # Match the user from the database
         user = UserMaster.objects.get(email=email)
         if user and user.password == password and user.role == role:
            if role == "Candidate":
               can = Candidate.objects.get(user_id=user)
               # Create sessions
               request.session["id"] = user.id
               request.session["role"] = user.role
               request.session["firstname"] = can.firstname
               request.session["lastname"] = can.lastname
               request.session["email"] = user.email
               return redirect("index")
            else:
               message = "Invalid role for login."
         else:
            message = "Invalid email or password."
      except UserMaster.DoesNotExist:
         message = "User does not exist."

      return render(request, "app/login.html", {"msg": message})
   else:
      return render(request, "app/login.html")
   
def ProfilePage(request):
   return render(request,"app/profile.html")
