from django.contrib import admin
from testapp.models import signup

# Register your models here.

class signup_admin(admin.ModelAdmin):
    list_display=[
        'Fname','Lname','password','rpassword'
    ]
admin.site.register(signup,signup_admin)
