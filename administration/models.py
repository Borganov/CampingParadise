from django.contrib.gis.db import models

# Create your models here.


class Arbres (models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)

    class Meta:
        db_table = "arbres"


class Batiments (models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)

    class Meta:
        db_table = "batiments"


class Emplacements (models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)

    class Meta:
        db_table = "emplacements"


class Piscines (models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)

    class Meta:
        db_table = "piscine"


class ZoneCamping (models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)

    class Meta:
        db_table = "zone-camping"
