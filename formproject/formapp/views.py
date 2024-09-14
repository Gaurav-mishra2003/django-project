from django.shortcuts import render
from formapp.forms import student_form

# Create your views here.
def student_view(request):
    submitted=False
    sname=''
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            sname=form.cleaned_data['name']
            print('name',form.cleaned_data['name'])
            print('name',form.cleaned_data['marks'])
            print('name',form.cleaned_data['rollno'])
            submitted=True
    form=student_form()  
    return render(request,'formapp/form.html',{'form':form, 'submitted':submitted ,'sname':sname})
