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



@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
def course_details(request,course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Exception as e:
        return Response({"error":"course does not found"})

    if request.method == "GET":
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    
    if request.method == "PUT":
        serializer = CourseSerializer(course, data = request.data)
        #(যখন PUT/PATCH করতে হবে কিন্তু সব ফিল্ড পাঠানো হবে না, তখন serializer errors দেবে।partial=True দিলে missing fields নিয়ে error দেবে না।
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    
    if request.method == "DELETE":
        course.delete()
        return Response({"massage":"course deleted successfully"}, status=204)



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

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
def subject_details(request,subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
    except Exception as e:
        return Response({"error":"subject does not found"})

    if request.method == "GET":
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    
    
    if request.method == "PUT":
        serializer = SubjectSerializer(subject, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    
    if request.method == "DELETE":
        subject.delete()
        return Response({"massage":"sunject deleted successfully"}, status=204)
