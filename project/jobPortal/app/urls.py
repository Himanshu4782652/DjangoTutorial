from django.urls import path,include
from . import views

urlpatterns = [
  path("",views.IndexPage,name="index"), 
  path("signup/",views.SignupPage,name="signup"),
  path("register/",views.RegisterUser,name="register"),
  # path("registercompany/",views.RegisterCompany,name="registercompany"),
  path("otppage/",views.OTPPage,name="otppage"),
  path("otp/",views.Otpverify,name="otp"),
  path("loginpage/",views.Loginpage,name="loginpage"),
  path("loginuser/",views.LoginUser,name="login"),
  path("profile/<int:pk>",views.ProfilePage,name="profile"),
  path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
  
  ############# Company Side ###############
  path("companyindex/",views.CompanyIndexPage,name="companyindex"),
  path("companyProfile/<int:pk>",views.CompanyProfile,name="companyProfile"),
  path("updatecompanyprofile/<int:pk>",views.CompanyProfileUpdate,name="updatecompanyprofile"),
]