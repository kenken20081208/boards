from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=200)
    kcal = models.PositiveIntegerField()
