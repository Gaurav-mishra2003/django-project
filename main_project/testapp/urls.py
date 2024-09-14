from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view),
    path('emp_page/',views.employee_page_view),
    path('blog_page/',views.blog_page_view)
]