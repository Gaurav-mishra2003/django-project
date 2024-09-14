from django.shortcuts import render
from blogapp.forms import blog_form
# Create your views here.

def blog_view(request):
    submitted=False
    name=''
    about=''
    if request.method=='POST':
        blog=blog_form(request.POST)
        if blog.is_valid():
            print(blog.cleaned_data['title'])
            print(blog.cleaned_data['about'])
            name=blog.cleaned_data['title']
            about=blog.cleaned_data['about']
            submitted=True
    blog=blog_form()
    return render(request,'bloagapp/blog.html',{'blog':blog, 'submitted':submitted,'name':name,'about':about})
