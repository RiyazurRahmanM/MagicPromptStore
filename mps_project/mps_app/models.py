from django.db import models

# Create your models here.

class Prompts(models.Model):
    name = models.TextField(max_length=30,default="NULL")
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    prompt = models.TextField(max_length=5000)
    price = models.FloatField(max_length=30,default=0.0)
    category = models.TextField(max_length=30,default='normal')
    sample_input = models.TextField(max_length=10000,default="null")
    sample_output = models.TextField(max_length=10000,default="null")

class Users(models.Model):
    name = models.TextField(max_length=30)
    email = models.TextField(max_length=50)
    password = models.TextField(max_length=10)
    prompts = models.ManyToManyField(Prompts)
    pending = models.ManyToManyField(Prompts,related_name='pending')

    
class Payment(models.Model):
    image = models.ImageField(upload_to="images/")
    delivery = models.TextField(default="Not Delivered")
    prompt = models.ForeignKey(Prompts,blank=True,null=True,on_delete=models.SET_NULL)
    user = models.ForeignKey(Users,blank=True,null=True,on_delete=models.SET_NULL)
    
class Delivery(models.Model):
    p = models.TextField()