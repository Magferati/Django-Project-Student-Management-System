from rest_framework import serializers
from .models import Teacher
from django.contrib.auth import get_user_model
from authentications.models import UserProfile
from authentications.serializers import UserProfileSerializer
from administration.serializers import CourseSerializer
from administration.models import Course
import random

User = get_user_model()

def generat_password():  #for random password it's use 
    return str(random.randint(100000,999999))

class TeacherSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)  # Add name as a write-only field for UserProfile
    last_name  = serializers.CharField(write_only=True) 
    phone_number  = serializers.CharField(write_only=True) 
    email  = serializers.EmailField(write_only=True) 
    profile_picture  = serializers.ImageField(write_only=True) 
    user = UserProfileSerializer(read_only = True)
    course = CourseSerializer(read_only = True)
    course_id = serializers.PrimaryKeyRelatedField(source='course', queryset=Course.objects.all(), write_only=True)

    class Meta:
        model = Teacher
        fields = ['id','user','first_name','last_name','designation','phone_number','email','profile_picture','course','course_id']

    def create(self,validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        phone_number = validated_data.pop('phone_number')
        profile_picture = validated_data.pop('profile_picture')
        designation = validated_data.pop('designation')
        course = validated_data.pop('course')
        password=generat_password()
        print("password", password)

        
        user = User.objects.create_user(
            email=validated_data['email'],
            password=password,
            role = validated_data.get('role', 'teacher')
        )
        profile = UserProfile.objects.create(
            user = user,
            first_name = first_name,
            last_name =  last_name
        )
        teacher=Teacher.objects.create(user=profile, designation=designation,course=course)
        return teacher

