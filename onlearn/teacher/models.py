from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.title




class Course(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    short_description = models.TextField( max_length=60,blank=True,null=True)
    description = models.TextField(blank=True)
    outcome = models.CharField(max_length=200,blank=True,null=True)
    requirements = models.CharField(max_length=200,blank=True,null=True)
    language = models.CharField(max_length=200,blank=True,null=True)
    price = models.FloatField(validators=[MinValueValidator(9.99)],blank=True,null=True)
    level = models.CharField(max_length=20,blank=True,null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',blank=True,null=True)
    video_preview = models.FileField(blank=True,null=True)
    video_lesson = models.FileField(blank=True,null=True)
    notes = models.TextField(blank=True)
    questions = models.TextField(blank=True)
    video_url = models.CharField(max_length=100,blank=True,null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    duration = models.FloatField(validators=[MinValueValidator(0.30), MaxValueValidator(30.00)])
    video_url = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
class Quiz(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,default=1)
    question = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    choice_five = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)