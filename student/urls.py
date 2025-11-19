from django.urls import path
from .views import student_list

urlpatterns = [
    path('add-student/', student_list),
    path('list-student/', student_list),
]
