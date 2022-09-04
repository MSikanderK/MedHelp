from django.contrib.gis.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    provider_type = models.CharField(max_length=50)