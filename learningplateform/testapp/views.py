from django.shortcuts import render
from testapp.models import Employee,Student_query_model
from . import forms

def greet(request):
    empdata=Employee.objects.all()
    emp_list={
        'emplist':empdata
    }
    return render(request,'testapp/index.html',context=emp_list)

def query_form_view(request):
    
    if request.method=='POST':
        form=forms.StudentQuery(request.POST) 
        if form.is_valid():
            user_name=form.cleaned_data['Name']
            user_rollno=form.cleaned_data['rollno']
            user_feedback=form.cleaned_data['feedback']
            student=Student_query_model(name=user_name,rollno=user_rollno,description=user_feedback)
            student.save()
           
            return render(request,'testapp/feedback.html')
            print('record added successfully')
    form=forms.StudentQuery()   
        
    

    return render(request,'testapp/query.html',{'form':form})