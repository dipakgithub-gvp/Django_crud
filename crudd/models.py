from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    employee_id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to="crud/images")

    def __str__(self):
        return self.name