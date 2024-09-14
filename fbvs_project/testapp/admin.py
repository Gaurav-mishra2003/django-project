from django.contrib import admin
from testapp.models import blog_model
from testapp.models import student_attendence,student_enrollment

# Register your models here.
admin.site_header='welcome to login'
admin.site_tittle='gauarav'
class blog_admin(admin.ModelAdmin):
    list_display=[
        'Title','Description','Publish_date'
    ]
admin.site.register(blog_model,blog_admin)


class Sattendence_admin(admin.ModelAdmin):
    list_display=[
        'Sname','Srollno','Sattendence','marks'

    ]
admin.site.register(student_attendence,Sattendence_admin)

class Senrollment_admin(admin.ModelAdmin):
    list_display=['Sname','SmobileNo','Saddress','ScourseName'

    ]
admin.site.register(student_enrollment,Senrollment_admin)