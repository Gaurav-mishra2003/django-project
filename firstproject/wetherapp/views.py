from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def greet_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    m='<h1>hello friends good '

    if h<12:
        m=m+'morning'
    elif h<16:
        m=m+'afternoon'
    elif h<21:
        m=m+'evening'
    else:
        m=m+'night'

    m=m+'</h1><hr>'+'<h1> the current date and time is '+str(date) +'</h1>'
    return HttpResponse(m)
