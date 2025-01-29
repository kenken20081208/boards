from django.db import models


class Borad(models.Model):
    moji = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
