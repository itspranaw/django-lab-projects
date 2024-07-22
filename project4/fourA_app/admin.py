from django.contrib import admin
from .models import Student,Course,Project

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','duration','code')
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','usn','cgpa')
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('name','usn','proj')