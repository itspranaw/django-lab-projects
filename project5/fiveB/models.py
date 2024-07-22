from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    usn = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name} {self.usn}'

class Course(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
