from django.db import models


# Create your models here.
class signup(models.Model):
    Fname=models.CharField(max_length=40)
    Lname=models.CharField(max_length=40)
    password=models.IntegerField()
    rpassword=models.IntegerField()
    

  

