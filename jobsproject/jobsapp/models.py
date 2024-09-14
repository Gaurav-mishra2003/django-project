from django.db import models


# Create your models here.
class hyd_jobs(models.Model):
    ename=models.CharField(max_length=30)
    eaddress=models.CharField(max_length=50)
    esallary=models.BigIntegerField()
    email=models.CharField(max_length=50)


