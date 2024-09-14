from django.db import models
import datetime


#categories models

class category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

# Create your models 
# customer modele.
class customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name}'
    
# all prodeucts


class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    category=models.ForeignKey(category,on_delete=models.CASCADEdefault,default=1)
    description=models.CharField(max_length=250,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/')
    def __str__(self):
        return self.name
    

class order(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    cutomer=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.IntegerField9

