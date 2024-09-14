from django.db import models
from django.db.models.signals import post_save 

# Create your models here.
from django.contrib.auth.models import User

# create a user profile models
class Profile(models.Model):
 # one to one relationship mean one user can have single profile and one profile have only single user 
 # on_delete cascade=mean when profile delete user will also delete
    user=models.OneToOneField(User,on_delete=models.CASCADE)
# stmetrical=false means if i follow anyone then its not compulsurry that otherone follow back to me
# blank=true ,eans you can follow or not its your Choice
#  manty to many field define that you can follw multiple peoples and multiple peaople can follw you

    follows=models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)
    date_modified=models.DateTimeField(User,auto_now=True)
    def __str__(self):
        return self.user.username
    


# lecture 3
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile=Profile(user=instance)    # this line use when user create then profile will automatically bn jayegi 
        user_profile.save()                   #user data save into userprofile
    #    when user created then it will follow which so profile id mean jaise hi user create ho he follow themselves automatically
        user_profile.follows.set([instance.profile.id]) 
        user_profile.save()      

post_save.connect(create_profile,sender=User)


# lecture 4




