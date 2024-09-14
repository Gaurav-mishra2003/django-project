from django.shortcuts import render
from jobsapp.models import hyd_jobs

# Create your views here.
def home_view(request):
    return render(request,'jobsapp/home.html')


def hyd_jobs_view(request):
    list_info=hyd_jobs.objects.all()
    dict={
        'list_info':list_info
    }
    return render(request,'jobsapp/hyd.html',dict)
