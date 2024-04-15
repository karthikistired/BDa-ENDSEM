# models.py

from django.db import models

class FoodIntake(models.Model):
    name = models.CharField(max_length=100)
    fats = models.FloatField()
    carbs = models.FloatField()
    protein = models.FloatField()

    @property
    def calories(self):
        return (self.fats * 9) + (self.carbs * 4) + (self.protein * 4)
