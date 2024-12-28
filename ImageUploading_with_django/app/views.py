from django.shortcuts import render,redirect
from .models import *

# Create your views here.

#index file view
def IndexPage(request):
 return render(request,"app/index.html")

#Upload image view
def ImageUpload(request):
 if request.method=="POST":
  imagename=request.POST['imgname']
  pics=request.FILES['image']
  #upload image
  newimg=ImageData.objects.create(Imagename=imagename,Image=pics)
  return redirect('show')
 
#image fetching view
def ImageFetch(request):
 all_img=ImageData.objects.all()
 return render(request,"app/show.html",{'key1':all_img})