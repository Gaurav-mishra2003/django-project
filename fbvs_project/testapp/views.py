from django.shortcuts import render,redirect,HttpResponse
from testapp.models import blog_model,student_attendence,student_enrollment
from testapp.forms import blog_form, SignUpForm,Sattedence_form,Senrollment_form
from django.contrib.auth.decorators import login_required
from django.views.generic import *



# Create your views here.


# @login_required
def home_page_view(request):
    return render(request,'testapp/home.html')
@login_required
def show_blog_view(request):
    list_items=blog_model.objects.all()
    return render(request,'testapp/show_blog.html',{'list_items':list_items})
@login_required
def insert_blog_view(request):
    form=blog_form()
    if request.method=='POST':
        form=blog_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/')
    return render(request,'testapp/blog_form.html',{'form':form})

@login_required
def delete_blog_view(request,id):
    blog=blog_model.objects.get(id=id)
    blog.delete()
    return redirect('/')
@login_required
def update_blog_view(request,id):
    blog=blog_model.objects.get(id=id)
    if request.method=='POST':
        form=blog_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/')
    return render(request,'testapp/update_blog.html',{'blog':blog})

def student_home_view(request):
    return render(request,'testapp/student_home.html')
    
    


def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        
        return redirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
    
# student section views
@login_required
def Sattendence_insert_view(request):
    form=Sattedence_form()
    if request.method=='POST':
        form=Sattedence_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/student/')
    return render(request,'testapp/sattendence_form.html',{'form':form})

@login_required
def sattendence_show_view(request):
    list_items=student_attendence.objects.all()
    return render(request,'testapp/show_attendence.html',{'list_items':list_items})

# course enrollment form enrolled student data form

def senrollment1_form(request):
    form=Senrollment_form()
    if request.method=='POST':
        form=Senrollment_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/student/')
    return render(request,'testapp/senrollment_form.html',{'form':form})

def senrolled_view(request):
    list_item=student_enrollment.objects.all()
    return render(request,'testapp/senrolled.html',{'list_items':list_item})

