from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    date_hired = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
