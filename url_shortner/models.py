"""Url short-ner models."""
from django.db import models


class Url(models.Model):
    """Url models."""

    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'shortner_url'
