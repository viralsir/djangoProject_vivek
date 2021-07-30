from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=70)
    address=models.TextField()
    phno=models.CharField(max_length=10)
    salary = models.IntegerField()

