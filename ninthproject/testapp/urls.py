from django.urls import path
from testapp import views

urlpatterns=[
    path('',views.testing_view),
    path('/more',views.more_view),
]