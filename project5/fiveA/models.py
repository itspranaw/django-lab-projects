from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    usn = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.usn}'