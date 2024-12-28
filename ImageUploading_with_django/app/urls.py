from django.urls import path,include
from . import views

urlpatterns = [
 path("",views.IndexPage,name="index"),
 path("upload/",views.ImageUpload,name="imageupload"),
 path('showing/',views.ImageFetch,name="show")
]
