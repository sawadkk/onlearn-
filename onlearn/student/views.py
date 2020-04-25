from django.shortcuts import render,redirect
from teacher.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from teacher.models import *
from student.models import *
from django.db import models	

def home(request):
	course = Course.objects.all()
	category = Category.objects.all()
	content = {'data':category,'datas':course}
	return render(request,'onlearn/home.html',content)
def addcart(request,a):
	ob = Course.objects.get(id=a)
	
	current_user = request.user
	if cart.objects.filter(course=a,user_id=current_user).count() < 1:
		cs = cart.objects.create(user=request.user,course=ob)
		messages.info(request,"course added to the cart")		
		return redirect('home')
		
	else:
		messages.info(request,"already exist in the cart")		
		return redirect('home')
def cartpage(request):
	ob = cart.objects.filter(user=request.user)
	#for c in ob:
		#name = c.course.title
		#price = c.course.price
		#print(name,"   ",price,"now")
	return render(request,'onlearn/student/cart.html',{'datas':ob})
def buy(request,a):
	
		ob = Course.objects.get(id=a)
		if mycourses.objects.filter(course=a,user_id=request.user).count() == 0:
			mycourses.objects.create(user=request.user,course=ob)
			messages.info(request,"congrats,successfully buyed")
			return redirect('home')
		else:
			messages.info(request,'already buyed this course')
			return redirect('home')
def mycourse(request):
	ob  = mycourses.objects.filter(user=request.user)
	return render(request,'onlearn/student/mycourses.html',{'datas':ob})
def cart_delete(request,a):
	
	cart.objects.get(id=a).delete()
	messages.success(request,'course deleted')
	return redirect(request.META['HTTP_REFERER'])

def search(request):
	data = request.GET.get('txtsearch')
	course = Course.objects.all().filter(title__icontains =data)
	return render(request,'onlearn/search.html',{'datas':course})
def addreview(request,a):
	course_id = Course.objects.get(id=a)
	if request.method=="POST":
		review = request.POST['review']
		reviews.objects.create(user=request.user,course=course_id,review=review)
		return redirect(request.META['HTTP_REFERER'])