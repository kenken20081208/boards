from django.db import models


class Borad(models.Model):
    moji = models.CharField(max_length=400)