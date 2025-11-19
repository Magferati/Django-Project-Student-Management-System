from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.decorators import api_view, permission_classes
from .models import Student
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()
#for course....................
@api_view(["GET" , "POST"])
@permission_classes([IsAuthenticated])

def student_list(request):
    if request.method == "GET":
        course = Student.objects.all()
        serializer = StudentSerializer(course, many = True)  # ekhane onek gula course thakte pare ejonno many true diyesi.

        return Response(serializer.data, status=200)
    if request.method == "POST":

        email = request.data.get('email')
        user_email = User.objects.filter(email=email).first()
        if user_email:
            return Response({'massage':'this email already exit'},status=400)

        serializer = StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'massage':'student addad successfully',
                 "data":serializer.data
            }
            return Response(context, status=201)

    return Response(serializer.errors, status=400)