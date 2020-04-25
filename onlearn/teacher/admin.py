from django.contrib import admin
from teacher.models import *
from account.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Quiz)