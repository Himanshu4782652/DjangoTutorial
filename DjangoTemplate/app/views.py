from django.shortcuts import render

# Create your views here.
#index.html view
def IndexView(request):
 return render(request, "app/index.html")

def htmlForm(request):
 return render(request, "app/forms.html")