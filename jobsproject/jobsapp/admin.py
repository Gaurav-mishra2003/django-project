from django.contrib import admin
from jobsapp.models import hyd_jobs
# Register your models here.
class hyd_admin(admin.ModelAdmin):
    list_display=['ename','eaddress','esallary','email']

admin.site.register(hyd_jobs,hyd_admin)



