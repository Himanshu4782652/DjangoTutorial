from django.urls import path,include
from . import views

urlpatterns = [
  path("",views.IndexPage,name="index"), 
  path("signup/",views.SignupPage,name="signup"),
  path("register/",views.RegisterUser,name="register"),
  path("registercompany/",views.RegisterCompany,name="registercompany"),
  path("otppage/",views.OTPPage,name="otppage"),
  path("otp/",views.Otpverify,name="otp"),
]