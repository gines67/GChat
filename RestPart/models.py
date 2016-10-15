from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class RoomCircle(models.Model):
	"""docstring for ClassName"""
	label = models.CharField(max_length=30, blank=True)
	id_client = models.ForeignKey(User)
	latCenter = models.FloatField()
	longCenter = models.FloatField()
	radius = models.FloatField()
	countConnect = models.IntegerField()

class RoomRect(models.Model):
	"""docstring for ClassName"""
	label = models.CharField(max_length=30,blank=True)
	countConnect = models.IntegerField()
	id_client = models.ForeignKey(User)
	lat1 = models.FloatField()
	long1 = models.FloatField()
	lat2 = models.FloatField()
	long2 = models.FloatField()
	lat3 = models.FloatField()
	long3 = models.FloatField()
	lat4 = models.FloatField()
	long4 = models.FloatField()
		
		

# Create your models here.
