from django.contrib import admin
from testapp.models import blog

# Register your models here.
class blog_admin(admin.ModelAdmin):
    list_display=['created_by','Title','Descreption','created','updated']

admin.site.register(blog,blog_admin)

