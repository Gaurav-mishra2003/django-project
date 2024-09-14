from django.shortcuts import render,redirect
from .models import blog
from . forms import BlogForm

# Create your views here.
def home(request):
    
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
    form= BlogForm()
    return render(request,'home.html',{'form':form})


def blog_view(request):
    list_data=blog.objects.all()
    return render(request,'see_blog.html',{'list_data':list_data})


def update_view(request,pk):
    data=blog.objects.get(id=pk)
   
    if request.method=='POST':
        form=BlogForm(request.POST,instance=blog)
        form.save()
        return redirect('/')
    
    return render(request,'update.html',{'data_item':data})