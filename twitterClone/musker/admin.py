from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Profile
from django.db.models.signals import post_save    # used jb koi user create ho then profile bhi create ho so user create hone pr signal generate krne ke liye

# Register your models here.
# unregister group from the admin site 
admin.site.unregister(Group)
# mix profile into user 
class ProfileInline(admin.StackedInline):
    model=Profile

class userAdmin(admin.ModelAdmin):
    model=User
    fields=['username']
    inlines=[ProfileInline]       #to mix up user and profile

# unregister users from the admin site  to make limited number of fields
admin.site.unregister(User)

# register again user with given limited firls
admin.site.register(User,userAdmin) 
# register Profile
#admin.site.register(Profile)   commented becouse we fixed up user and profile both in single one 



# lecture 4


