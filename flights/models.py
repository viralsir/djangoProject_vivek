from django.db import models

# makemigrations
# migrate

# Create your models here.
class flight(models.Model):
    origin=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destination}"