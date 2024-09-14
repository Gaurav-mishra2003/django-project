from django.db import models
from datetime import *

# Create your models here.
class senrollment_model(models.Model):
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=39)
    course=models.CharField(max_length=40)
    mobile_no=models.BigIntegerField()
    Date=models.DateField(default='datetime.datetime.now()')



class student_attendence(models.Model):
    Name=models.CharField(max_length=50)
    Attendence=models.CharField(max_length=1)
    Branch=models.CharField(max_length=30)
    Date=models.DateField()

