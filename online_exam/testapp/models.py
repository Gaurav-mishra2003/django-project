from django.db import models

# Create your models here.
class student_test_model(models.Model):
    ques=models.CharField(max_length=200)
    opt1=models.CharField(max_length=50)
    opt2=models.CharField(max_length=50)
    opt3=models.CharField(max_length=50)
    opt4=models.CharField(max_length=50)
    ans=models.CharField(max_length=50)
    