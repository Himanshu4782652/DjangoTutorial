from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

#this view for display post view
def Index(request):
 posts=Post.objects.all()
 return render(request,"app/index.html",{'posts':posts})

#this view display the particular liked post
def likePost(request):
 if request.method=="GET":
  post_id=request.GET['post_id'] #post id
  likedpost=Post.objects.get(pk=post_id) #getting post which are like
  l=Like(post=likedpost) #creating like objects
  l.save() #saving it to store in database
  return HttpResponse("Success !")
 else:
  return HttpResponse("Request method is not GET")