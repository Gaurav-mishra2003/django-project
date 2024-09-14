from django.db import models

from django.contrib.auth.models import User
# Create your models here.\
class blog(models.Model):
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    Title=models.CharField(max_length=40)
    Descreption=models.CharField(max_length=200)
    created=models.DateField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

