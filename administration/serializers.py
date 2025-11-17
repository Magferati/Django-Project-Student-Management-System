from rest_framework import serializers
from .models import Course, Subject

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only = True)
    course_id = serializers.PrimaryKeyRelatedField(source='course', queryset=Course.objects.all(), write_only=True)
    class Meta:
        model = Subject
        fields = ["id","course","course_id","subject_name"]