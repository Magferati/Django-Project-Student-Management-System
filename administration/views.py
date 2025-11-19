from django.shortcuts import render

# Create your views here.
from .serializers import CourseSerializer, SubjectSerializer
from rest_framework.decorators import api_view, permission_classes
from .models import Course, Subject
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

#for course....................
@api_view(["GET" , "POST"])
@permission_classes([IsAuthenticated])

def course_list(request):
    if request.method == "GET":
        course = Course.objects.all()
        serializer = CourseSerializer(course, many = True)  # ekhane onek gula course thakte pare ejonno many true diyesi.

        return Response(serializer.data, status=200)
    if request.method == "POST":

        serializer = CourseSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


#for subject...............
@api_view(["GET" , "POST"])
@permission_classes([IsAuthenticated])

def subject_list(request):
    if request.method == "GET":
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many = True)  # ekhane onek gula subject thakte pare ejonno many true diyesi.

        return Response(serializer.data, status=200)
    if request.method == "POST":

        serializer = SubjectSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)