from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField()
    gender=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    sec=models.TextField(max_length=50)
    usn=models.TextField()
    cgpa=models.FloatField()

class Course(models.Model):
    name=models.CharField(max_length=100)
    duration=models.IntegerField()
    code=models.CharField(max_length=50)
    credits=models.IntegerField()
    fees=models.FloatField()