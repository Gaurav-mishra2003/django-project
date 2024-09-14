from django.shortcuts import render
from testapp.models import student_test_model

# Create your views here.
def home_view(request):
    list_question=student_test_model.objects.all()
    
    return render(request,'home.html',{'list_question':list_question})
    
