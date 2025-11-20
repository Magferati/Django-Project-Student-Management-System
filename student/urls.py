from django.urls import path
from .views import student_list, student_details

urlpatterns = [
    path('add-student/', student_list),
    path('list-student/', student_list),
    path('student_details/<int:student_id>/', student_details),
]
