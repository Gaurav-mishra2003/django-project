from django.contrib import admin
from testapp.models import student_test_model

# Register your models here.
class test_admin(admin.ModelAdmin):
    list_display=[
        'ques','opt1','opt2','opt3','opt4','ans'
    ]
admin.site.register(student_test_model,test_admin)

