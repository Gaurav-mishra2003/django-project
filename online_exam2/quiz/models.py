from django.db import models

# Create your models here.

   
class pythonquiz(models.Model):
    category=models.CharField(max_length=50,default='python')
    ques=models.CharField(max_length=100)
    opt1=models.CharField(max_length=50)
    opt2=models.CharField(max_length=50)
    opt3=models.CharField(max_length=50)
    opt4=models.CharField(max_length=50)
class javaquiz(models.Model):
    category=models.CharField(max_length=50,default='python')
    ques=models.CharField(max_length=100)
    opt1=models.CharField(max_length=50)
    opt2=models.CharField(max_length=50)
    opt3=models.CharField(max_length=50)
    opt4=models.CharField(max_length=50)
    

