from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


#to view signupform
def signupform(request):
	return render(request,'onlearn/account/signup.html')

#to view loginform
def loginform(request):
	return render(request,'onlearn/account/login.html')

#to signup
def signup_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.create_user(username=username,email=email,password=password)
		print("user created")
		messages.success(request,'user created successfully')
		login(request,user)
		print("userlogin")
		return redirect('home')
	else:
		return redirect('signupform')

#to login
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		User = authenticate(username=username,password=password)
		if User is not None:
			login(request,User)
			print("userlogin")
			return redirect('home')
		else:
			print("no such user")
			messages.info(request,'incorect username and password')
			return redirect('loginform')
	else:
		return redirect('loginform')

#to signout
def signout_user(request):
	logout(request)
	return redirect('home')

#to view account deatils
def myaccount(request):
	data = User.objects.filter(username=request.user)
	return render(request,'onlearn/account/myaccount.html',{'datas':data})


#to change password
def updatepassword(request):
	if request.method == "POST":
		form = PasswordChangeForm(user=request.user,data=request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'your password updated successfully')
			return redirect('myaccount')
		else:
			messages.error(request,'password requirments not met')
			form = PasswordChangeForm(request.user)
			return render(request,'onlearn/account/password.html',{'form':form})
	else:
		form = PasswordChangeForm(request.user)
		return render(request,'onlearn/account/password.html',{'form':form})

def delete_user(request):
	messages.info(request,'your data will be permentaly lost')
	User.objects.get(username=request.user).delete()
	messages.success(request,'user deleted')
	return redirect('home')

