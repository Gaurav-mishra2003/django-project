
from django.contrib import admin
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view),
    path('quiz/',views.quiz_view),
    path('accounts/',include('django.contrib.auth.urls')), 
    path('logout/',views.logout)
]
