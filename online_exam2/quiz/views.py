from django.shortcuts import render
from quiz.models import *

# Create your views here.
def quizview(request,id):
    que=javaquiz.objects.get(id=id)
   
    return render(request,'index.html',{'list':que})

def homeview(request):
    return render(request,'home.html')
    # que=javaquiz.objects.get(id=id)
   
    # return render(request,'home.html')
def getscore(request):
    list=javaquiz.objects.all()