from django.db import models


class Geometry(models.Model):
    geom_id = models.IntegerField(default=0)
    geom = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

