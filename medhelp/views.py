from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Provider

latitude = 31.482032
longitude = 74.295868

user_location = Point(longitude, latitude, srid=4326)

#views
class Home(generic.ListView):
    model = Provider
    context_object_name = "providers"
    queryset = Provider.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:11]
    template_name = "providers/index.html"
