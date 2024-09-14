from django.db import models


# Create your models here.
class student_model(models.Model):
    name=models.CharField(max_length=40)
    about=models.CharField(max_length=40)
