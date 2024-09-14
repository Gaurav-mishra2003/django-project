from django.shortcuts import render
from testapp.forms import blog_form

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

def create_form_view(request):
    form=blog_form()
    if request.method=='POST':
        form=blog_form(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            request.session[title]=description
            request.session.set_expiry(20)
            print(request.session)
           



            
    return render(request,'testapp/form.html',{'form':form})


def show_blog_view(request):
    
    print(type(request.session))
    return render(request,'testapp/showblog.html')


