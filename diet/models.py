from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=200)
    kcal = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
