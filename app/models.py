from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    division = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}-{self.student_class}"
