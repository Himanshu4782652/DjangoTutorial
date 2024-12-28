from django.shortcuts import render
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
  return render(request,"app/show.html")