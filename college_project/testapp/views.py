from django.shortcuts import render,redirect
from testapp.models import *
from testapp.forms import student_form

# Create your views here.
def home_page(request):
    return render(request,'testapp/home.html')
def student_page(request):
    return render(request,'testapp/s_homeview.html')

def student_course(request):
    return render(request,'testapp/course.html')


def student_enrollment(request):
    form=student_form()
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return redirect('/enrolled/')

        
    return render(request,'testapp/enrollment_form.html',{'form':form})


def student_attendence(request):
    return render(request,'testapp/attendence.html')

def student_enrolled(request):
    item_list=senrollment_model.objects.all()
    return render(request,'testapp/s_enrolled.html',{'list_items':item_list})

def student_assignments(request):
    return render(request,'testapp/assignment.html')