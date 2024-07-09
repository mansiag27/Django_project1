from django.db import models


# Create your models here.

class School(models.Model):
    school_id = models.CharField(primary_key=True, max_length=5,unique=True)
    school_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)

class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=5,unique=True)
    name = models.CharField(max_length=10)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=5)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class User(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    username = models.CharField(max_length=10,unique=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')






