from django.contrib import admin
from testapp.models import *

# Register your models here.
class enroll_admin(admin.ModelAdmin):
    list_display=[
      'name' ,'father_name' ,'course','mobile_no','Date'
    ]
admin.site.register(senrollment_model,enroll_admin)

class student_attendence_admin(admin.ModelAdmin):
    list_display=[
        'Name','Attendence','Branch','Date'
    ]
admin.site.register(student_attendence,student_attendence_admin)

