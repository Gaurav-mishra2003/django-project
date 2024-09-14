from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=30)
    esallary=models.IntegerField()
class Student_query_model(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    description=models.CharField(max_length=50)
