from django.shortcuts import render
from testapp.models import student_model
from testapp.forms import student_form


# Create your views here.
def create_form(request):
    form=student_form()
    if request.method=='POST':
        form=student_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'testapp/form.html',{'form':form})


def show_view(request):
    list_info=student_model.objects.all()
    return render(request,'testapp/show.html',{ 'list_info':list_info})