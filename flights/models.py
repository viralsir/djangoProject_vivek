from django.db import models

# makemigrations
# migrate
'''
  one to one  onetooneField
  one to many Foriegnkey
  many to many  ManytoManyField
'''
class airport(models.Model):
    code=models.CharField(max_length=30)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}({self.code})";


# Create your models here.
class flight(models.Model):
    origin=models.ForeignKey(airport,on_delete=models.CASCADE,related_name="departure")
    destination=models.ForeignKey(airport,on_delete=models.CASCADE,related_name="arrival")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destination}"