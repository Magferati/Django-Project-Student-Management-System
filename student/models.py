# from django.db import models
# from authentications.models import UserProfile
# from administration.models import Course
# # Create your models here.
# class Student(models.Model):
#     user = models.OneToOneField( UserProfile,on_delete=models.CASCADE ,blank=True, null=True,related_name='student')
#     roll_no = models.CharField(max_length=6)
#     course = models.ForeignKey(Course, on_delete=models.RESTRICT,blank=True, null=True)

#     def __str__(self):
#         return self.user.email if self.user else "No User"

from django.db import models

class Student(models.Model):
    user = models.OneToOneField(
        "authentications.UserProfile",   
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='student'
    )
    roll_no = models.CharField(max_length=6)
    course = models.ForeignKey(
        "administration.Course",       
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.first_name if self.user else "No User"
