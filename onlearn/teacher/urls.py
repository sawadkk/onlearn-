from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [url(r'^course_details(?P<a>\d+)',views.course_details,name='course_details'),
			   url(r'^exam(?P<a>\d+)',views.exam,name='exam'),
			   path('certificate',views.certificate,name = 'certificate'),
			   path('result',views.exam_result,name = 'result'),
               url(r'^course(?P<a>\d+)',views.course,name='course'),
               path('addcourse',views.addcourse,name="addcourse"),
               path('courseadd',views.courseadd,name="courseadd"),
               path('courses',views.courses,name = 'courses'),]


