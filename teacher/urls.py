from django.urls import path
from .views import teacher_list

urlpatterns = [
    path('add-teacher/', teacher_list),
    path('list-teacher/', teacher_list),
]
