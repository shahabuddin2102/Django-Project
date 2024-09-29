from django.db import models

# Create your models here.
class Student(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=12)
    coursename=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
