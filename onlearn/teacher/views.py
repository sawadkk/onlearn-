from django.shortcuts import render,redirect
from teacher.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse

# Create your views here.
def course_details(request,a):
	data = Course.objects.filter(id=a)
	return render(request,"onlearn/teacher/course_details.html",{'datas':data})

		
def course(request,a):
	data  = Course.objects.filter(id=a)
	return render(request,"onlearn/teacher/course.html",{'datas':data})

def addcourse(request):
	#if request.user.has_perm('app_name.can_add_course'):
		#messages.info(request,'upload your course')
		#return render(request,"onlearn/teacher/addcourse.html")
	#else:
		#messages.info(request,'you have no permission to add course')
	return render(request,"onlearn/teacher/addcourse.html")
def courseadd(request):
	if request.method == "POST":
		name = request.POST['name']
		short_description = request.POST['short_description']
		notes = request.POST['notes']
		price = request.POST['price']
		
		video_lesson = request.FILES['video_lesson']
		
		Course.objects.create(user=request.user,title=name,short_description=short_description,notes=notes,video_lesson=video_lesson,)
		messages.info(request,'course added successfully')
		return render(request,"onlearn/home.html")
def courses(request):
	course = Course.objects.all()
	category = Category.objects.all()
	content = {'data':category,'datas':course}
	return render(request,'onlearn/teacher/courses.html',content)

def exam(request,a):
	questions = Quiz.objects.filter(course=a)
	context = {'questions':questions}
	return render(request,'exam.html',context)
score = 0
	
def exam_result(request):
	questions = Quiz.objects.all()
	global score
	for question in questions:
		correct_answer = question.answer
		entered_answer = request.POST.get(str(question.id))
		if entered_answer == correct_answer:
			score+=1
	content = {'score':score}
	return render(request,'onlearn/teacher/result.html',content)
def certificate(request):
	data = Quiz.objects.all()
	global score
	context = {'score':score,'datas':data}
	if score >= 1:
		return render(request,'onlearn/teacher/certificate.html',context)
	else:
		messages.info(request,'you are not passed wish success on next attempt')
		return render(request,'onlearn/home.html')

