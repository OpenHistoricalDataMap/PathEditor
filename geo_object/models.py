from django.db import models

class GeoObject(models.Model):
    geom_id         = models.IntegerField(default=0)
    geom            = models.CharField(max_length=1000)
    pub_date        = models.DateTimeField(auto_now_add=True)
    description     = models.CharField(max_length=200)
    name            = models.CharField(max_length=50)
    valid_from      = models.DateTimeField()
    valid_until     = models.DateTimeField()
    source          = models.URLField(null=True)

    def __str__(self):
        return (self.name + '(ID: '+ str(self.id) +' Geo-ID: '+ str(self.geom_id) + self.source +')')
