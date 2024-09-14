"""
URL configuration for fbvs_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from testapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page_view),                                     
    path('showblog/',views.show_blog_view),
    path('insertblog/',views.insert_blog_view),
    path('delete/<int:id>',views.delete_blog_view),
    path('update/<int:id>',views.update_blog_view),
    path('accounts/',include('django.contrib.auth.urls')),

    # for class base view
    path('student/',views.student_home_view),
    path('signup/',views.signup),
    path('attendence/',views.Sattendence_insert_view),
    path('show_attendence/',views.sattendence_show_view),
    path('enrollment/',views.senrollment1_form),
    path('enrolled/',views.senrolled_view)
 
]
