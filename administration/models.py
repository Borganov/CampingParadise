from django.contrib.gis.db import models

# Create your models here.

class Arbres (models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.PositiveIntegerField(null=True)
    geom = models.MultiPolygonField(srid=4326, null=True)

    class Meta:
        db_table = "arbres"