from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.views.generic import *

# Create your views here.
def home_view(request):
    return render(request,'index.html')
@login_required
def quiz_view(request):
    return render(request,'quiz.html')

def logout(request):
    return render(request,'logout.html')