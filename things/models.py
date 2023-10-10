from django.db import models


class Thing(models.Model):
    name = models.CharField(
        blank=False,
        unique=True,
        max_length=30
    )
    description = models.CharField(
        blank=True,
        unique=False,
        max_length=120
    )
    quantity = models.IntegerField(
        min=0,
        max=0
    )
