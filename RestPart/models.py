from __future__ import unicode_literals

from django.db import models

class RoomCircle(models.Model):
	"""docstring for ClassName"""
	label = models.CharField(max_length=30, blank=True)
	latCenter = models.FloatField()
		

# Create your models here.
