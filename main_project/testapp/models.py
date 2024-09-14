from django.db import models

# Create your models here.
class employee_model(models.Model):
    ename=models.CharField(max_length=100)
    enumber=models.BigIntegerField()
    esallary=models.BigIntegerField()
    eaddress=models.CharField(max_length=200)
  

class blog_model(models.Model):
    bname=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date=models.DateField()