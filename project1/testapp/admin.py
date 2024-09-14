from django.contrib import admin
from testapp.models import student_model

# Register your models here.
class student_admin(admin.ModelAdmin):
    list_display=[
        'name','about'
    ]
admin.site.register(student_model,student_admin)
