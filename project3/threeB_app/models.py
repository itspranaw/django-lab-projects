from django.db import models

class Project(models.Model):
    name=models.CharField(max_length=100)
    usn=models.TextField(max_length=50)
    proj=models.CharField(max_length=100)
    lang=models.CharField(max_length=100)
    duration=models.IntegerField()