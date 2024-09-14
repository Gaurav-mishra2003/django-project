from django.shortcuts import render
from . forms import signup

# Create your views here.
def form_validation_view(request):
    
    if request.method=='POST':
        form=signup(request.POST)
        if form.is_valid():
            print('entered name id ',form.cleaned_data['name'])
    
    form=signup() 
    return render(request,'signup.html',context={'form':form})
