from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [path('loginform',views.loginform,name = "loginform"),
			   path('signupform',views.signupform,name = "signupform"),
			   path('signup',views.signup_user,name = "signup"),
			   path('login',views.login_user,name = "login"),
			   path('signout',views.signout_user,name = "signout"),
			   path('myaccount',views.myaccount,name = "myaccount"),
			   url(r'^password/$',views.updatepassword,name = "updatepassword"),
			   path('delete_user',views.delete_user,name = "delete_user"),
			   ]