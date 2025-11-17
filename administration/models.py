from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from student.models import Student
#from administration.models import Course
# Create your models here.

    
class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
    
class Subject(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="subject_name")
    subject_name= models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name
    
class Enrolment(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE, related_name="student")
    subject = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="subject" )