from django.shortcuts import render
from .forms import Student_Form
from testapp.forms import Student_Form
from django import forms


# Create your views here
def student_view(request):
    form=Student_Form()
    return render(request,'testapp/index.html' ,{'form':form})
