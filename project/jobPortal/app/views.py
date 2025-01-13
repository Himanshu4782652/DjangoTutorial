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
               if role == "Company":
                  com=Company.objects.get(user_id=user)
                  # Create sessions
                  request.session["id"] = user.id
                  request.session["role"] = user.role
                  request.session["firstname"] = com.firstname
                  request.session["lastname"] = com.lastname
                  request.session["email"] = user.email
                  return redirect("companyindex")
         else:
            message = "Invalid email or password."
      except UserMaster.DoesNotExist:
         message = "User does not exist."

      return render(request, "app/login.html", {"msg": message})
   else:
      return render(request, "app/login.html")
   
def ProfilePage(request,pk):
   user=UserMaster.objects.get(pk=pk) 
   can=Candidate.objects.get(user_id=user)
   return render(request,"app/profile.html",{'user':user, 'can':can})

def UpdateProfile(request,pk):
   user=UserMaster.objects.get(pk=pk)
   if user.role=="Candidate":
      can=Candidate.objects.get(user_id=user)
      # breakpoint()
      can.country=request.POST['country'] #first country belongs to database field and second field is belongs to html input name
      can.state=request.POST['state']
      can.city=request.POST['city']
      can.job_type=request.POST['job_type']
      can.jobcategory=request.POST['jobcategory']
      can.highestedu=request.POST['highestedu']
      can.experience=request.POST['experience']
      can.website=request.POST['website']
      can.shift=request.POST['shift']
      can.jobdescription=request.POST['jobdescription']
      can.min_salary=request.POST['min_salary']
      can.max_salary=request.POST['max_salary']
      can.contact=request.POST['contact']
      can.gender=request.POST['gender']
      can.profile_pic=request.FILES['profile_pic']
      can.save()
      url=f'/profile/{pk}' #formatting url
      return redirect(url)
   
   
########## Company Side ###########

def CompanyIndexPage(request):
   return render(request,"app/company/index.html")

def CompanyProfile(request):
   return render(request,"app/company/profile.html")