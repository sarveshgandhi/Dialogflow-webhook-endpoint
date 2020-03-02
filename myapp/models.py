from django.db import models

# Create your models here.
class Person(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    def __str__(self):
        return f"height = {self.height}, weight = {self.weight}, bmi = {self.bmi}"