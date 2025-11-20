from django.urls import path
from .views import course_list , subject_list, course_details,subject_details

urlpatterns = [
    path('course/', course_list),
    path('subject/', subject_list),
    path('course-details/<int:course_id>/', course_details),
    path('subject_details/<int:subject_id>/', subject_details),
]
