from django.shortcuts import render
from .models import Profile

# Create your views here.
def home(request):
    return render(request,'home.html')

def profile_list(request):
    # exclude means only show page when user is login otherwise it will give error 
    if request.user.is_authenticated:
         profiles=Profile.objects.exclude(user=request.user)   
         return render(request,'profile_list.html',{'profiles':profiles})
    else:
        return render(request,'error.html') 

   
   
