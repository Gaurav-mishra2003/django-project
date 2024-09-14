from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('',views.home_page),
  path('s_home/',views.student_page),
  path('course/',views.student_course),
  path('enrolled/',views.student_enrolled),
  path('attendence/',views.student_attendence),
  path('assignment/',views.student_assignments),
  path('student_enroll/',views.student_enrollment)
]
