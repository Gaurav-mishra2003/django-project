from django.contrib import admin
from testapp.models import Employee,Student_query_model

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=[
        'ename','esallary'
    ]
class student_query_admin(admin.ModelAdmin):
    list_display=[
        'name','rollno','description'
    ]
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Student_query_model,student_query_admin)
