from django.contrib import admin
from testapp.models import blog_model,employee_model

# Register your models here.
class employee_admin(admin.ModelAdmin):
    list_display=[
        'ename','enumber','esallary','eaddress'
    ]

class blog_admin(admin.ModelAdmin):
    list_display=[
        'bname','description','date'
    ]

admin.site.register(employee_model,employee_admin)
admin.site.register(blog_model,blog_admin)
