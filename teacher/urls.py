from django.urls import path
from .views import teacher_list,teacher_details

urlpatterns = [
    path('add-teacher/', teacher_list),
    path('list-teacher/', teacher_list),
    path('teacher_details/<int:teacher_id>/', teacher_details),
]
