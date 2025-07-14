from django.db import models

# Create your models here.

class task(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    description=models.CharField(max_length=400)
    isDone=models.BooleanField(default=False)

    def __str__(self):
        return ("f{self.name}+{self.date}")  