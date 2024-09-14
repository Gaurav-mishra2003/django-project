
from . import views
from django.urls import path

urlpatterns = [
  path('greet/',views.greet)
]