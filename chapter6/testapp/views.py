from django.shortcuts import render
from . models import signup
from .forms import signupform

# Create your views here.

def signupform_view(request):
   
   if request.method=='POST':
      form=signupform(request.POST)
      if form.is_valid():
         form.save()
   form=signupform()
   return render(request,'testapp/signup.html',{'form':form})
