from rest_framework import serializers
from .models import Student
from django.contrib.auth import get_user_model
from authentications.models import UserProfile
from authentications.serializers import UserProfileSerializer
from administration.serializers import CourseSerializer
from administration.models import Course

User = get_user_model()

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True, required=False)
    last_name  = serializers.CharField(write_only=True, required=False)
    phone_number  = serializers.CharField(write_only=True, required=False)
    email  = serializers.EmailField(write_only=True, required=False)
    profile_picture  = serializers.ImageField(write_only=True, required=False)

    user = UserProfileSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(source='course', queryset=Course.objects.all(), write_only=True, required=False)

    class Meta:
        model = Student
        fields = [
            'id','user','first_name','last_name','roll_no',
            'phone_number','email','profile_picture',
            'course','course_id'
        ]

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        phone_number = validated_data.pop('phone_number')
        profile_picture = validated_data.pop('profile_picture')
        roll_no = validated_data.pop('roll_no')
        course = validated_data.pop('course')
        email = validated_data.pop('email')

        user = User.objects.create_user(
            email=email,
            password=roll_no,
            role='student'
        )

        profile = UserProfile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            profile_picture=profile_picture
        )

        student = Student.objects.create(
            user=profile, roll_no=roll_no, course=course
        )
        return student


    def update(self, instance, validated_data):
        # Update Student fields
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)

        # Update course if provided
        course = validated_data.get('course', None)
        if course:
            instance.course = course

        # Update UserProfile
        profile = instance.user
        profile.first_name = validated_data.get('first_name', profile.first_name)
        profile.last_name = validated_data.get('last_name', profile.last_name)
        profile.phone_number = validated_data.get('phone_number', profile.phone_number)

        if 'profile_picture' in validated_data:
            profile.profile_picture = validated_data['profile_picture']

        profile.save()

        # Update User model
        user = profile.user
        if 'email' in validated_data:
            user.email = validated_data['email']
        user.save()

        instance.save()
        return instance
