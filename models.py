from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)   # e.g. "Accountant", "Librarian", "Peon"
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name