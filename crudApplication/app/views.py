from django.shortcuts import render
from .models import *
# Create your views here.
def InsertPageView(request):
 return render(request,"app/insert.html")

def InsertData(request):
 #data came from html to view
 fname=request.POST['fname']
 lname=request.POST['lname']
 email=request.POST['email']
 contact=request.POST['contact']
 
 #creating object of model class
 #inserting data into table
 newuser=Student.objects.create(Firstname=fname,Lastname=lname,
                                Email=email,Contact=contact)
 
 #after insert render on show.html
 return render(request,"app/show.html")