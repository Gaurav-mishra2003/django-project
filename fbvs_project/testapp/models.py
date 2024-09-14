from django.db import models

# Create your models here.
class blog_model(models.Model):
    Title=models.CharField(max_length=40)
    Description=models.TextField()
    Publish_date=models.DateField()

class student_attendence(models.Model):
    Sname=models.CharField(max_length=40)
    Srollno=models.IntegerField()
    Sattendence=models.CharField(max_length=1)
    marks=models.IntegerField()

class student_enrollment(models.Model):
    Sname=models.CharField(max_length=40)
    SmobileNo=models.BigIntegerField()
    Saddress=models.CharField(max_length=50)
    ScourseName=models.CharField(max_length=50)