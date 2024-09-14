from django.shortcuts import render
from testapp.models import student
from django.core.paginator import Paginator

# Create your views here.
def home_page_view(request):
    list_items=student.objects.all()


    #pagination  first argument is iterable and second argumnet is number page want to show in pr page
    p=Paginator(list_items,2)
    # to track number of pages
    page=request.GET.get('page')
    list_items1=p.get_page(page)
  
    return render(request,'index.html',{'list_items':list_items,'list_items1':list_items1})
