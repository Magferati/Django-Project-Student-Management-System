from django.db import models
from authentications.models import UserProfile
from administration.models import Course
# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(
        "authentications.UserProfile",   
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='teacher'
    )
    designation = models.CharField(max_length=200,blank=True,null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return self.user.first_name if self.user else "No User"