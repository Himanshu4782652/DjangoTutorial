from django.shortcuts import render

# Create your views here.

#view for register page
def RegisterPage(request):
 return render(request,"app/register.html")