from django.contrib import admin
from quiz.models import *

# Register your models here.
class admin1(admin.ModelAdmin):
    list_display=[
        'category','ques','opt1','opt2','opt3','opt4'
    ]
class admin2(admin.ModelAdmin):
    list_display=[
        'category','ques','opt1','opt2','opt3','opt4'
    ]
admin.site.register(pythonquiz,admin1)
admin.site.register(javaquiz,admin2)
