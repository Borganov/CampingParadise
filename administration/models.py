from django.contrib.gis.db import models


# Create your models here.


class Arbres(models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)

    class Meta:
        db_table = "arbres"


class Services(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nom = models.CharField(max_length=200, null=True)
    marker = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "services"


class Batiments(models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    name = models.CharField(max_length=200)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return self.gid

    class Meta:
        db_table = "batiments"


class Emplacements(models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    booked = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.gid

    class Meta:
        db_table = "emplacements"


class Piscines(models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "piscine"


class ZoneCamping(models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    id = models.BigIntegerField(null=True)
    geom = models.MultiPolygonField(srid=3857, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "zone-camping"


class Reservations(models.Model):
    gid = models.PositiveSmallIntegerField(primary_key=True)
    emplacement_gid = models.ForeignKey(Emplacements, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, null=True)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    factureFinale = models.FloatField()

    class Meta:
        db_table = "reservations"
