from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reading(models.Model):
    time = models.DateTimeField()
    weight = models.FloatField()
