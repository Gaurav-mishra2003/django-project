from django.shortcuts import render

# Create your views here.
def testing_view(request):
    dic={
        'msg':'thankyou '
    }
    return render(request,'testapp_templates/index.html',context=dic)

def more_view(request):
    dic={
        'msg':'more'
    }
    return render(request,'testapp_templates/index.html',context=dic)
