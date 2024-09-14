from django.shortcuts import render
from testapp.models import employee_model,blog_model


# Create your views here.

def home_view(request):
    return render(request,'testapp/home.html')

def employee_page_view(request):
    list_item=employee_model.objects.all()
    return render(request,'testapp/employee_page.html',{'list_item':list_item})

def blog_page_view(request):
   
    list_item=blog_model.objects.all()
    return render(request,'testapp/blog_page.html',{'list_item':list_item})


