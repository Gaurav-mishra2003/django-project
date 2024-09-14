from django.shortcuts import render
import datetime

# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()


    hours=int(date.strftime('%H'))
    if hours<12:
        msg1='good morning'
    elif hours<16:
        msg1='good afternoon'
    elif hours <21:
        msg1='good evening'
    else:
        msg1='good night'
    info={
        'msg':date,
        'msg1':msg1
    }
    return render(request,'firstapp/index.html',context=info)
