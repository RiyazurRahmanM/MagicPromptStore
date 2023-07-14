from django.db import models

# Create your models here.

class Prompts(models.Model):
    name = models.TextField(max_length=30,default="NULL")
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=500)
    prompt = models.TextField(max_length=5000)
    price = models.FloatField(max_length=30)

class Payment(models.Model):
    image = models.ImageField(upload_to="images/")

class Users(models.Model):
    name = models.TextField(max_length=30)
    email = models.TextField(max_length=50)
    password = models.TextField(max_length=10)

