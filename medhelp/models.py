from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    provider_type = models.CharField(max_length=50)