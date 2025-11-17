from django.db import models
from authentications.models import UserProfile
from administration.models import Course
# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField( UserProfile,on_delete=models.CASCADE ,blank=True, null=True,related_name='teacher')
    roll_no = models.CharField(max_length=6)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return self.user.email if self.user else "No User"