from django.db import models
from geo_object.models import GeoObject
from sortedm2m.fields import SortedManyToManyField

class StoryPath(models.Model):
    #spots           = SortedManyToManyField(GeoObject, sort_value_field_name='spot_id')
    spots           = models.ManyToManyField(GeoObject)
    pub_date        = models.DateTimeField(auto_now_add=True)
    description     = models.CharField(max_length=200, default="Info about Path")
    name            = models.CharField(max_length=50, default="New Path")
    valid_from      = models.DateTimeField(null=True)
    valid_until     = models.DateTimeField(null=True)
    source          = models.URLField(null=True)

