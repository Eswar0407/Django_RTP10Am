from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return self.name