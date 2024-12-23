from django.urls import path, include
from .import views
urlpatterns = [
 path("",views.InsertPageView,name="insertPage"),
 path("insert/",views.InsertData,name="insert"),
 path("showPage/",views.ShowPage, name="showPage")
]