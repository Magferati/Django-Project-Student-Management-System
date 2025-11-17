from django.urls import path
from .views import course_list , subject_list

urlpatterns = [
    path('course/', course_list),
    path('subject/', subject_list),
]
