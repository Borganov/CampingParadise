from administration.models import Piscines, Arbres, Emplacements, Batiments, ZoneCamping
from shapely.geometry import shape, Point
from django.core.serializers import serialize
import geopandas as gpd


class campingDetails:
    camping_area = 1
    tree_count = -1
    zone_count = -1
    emplacement_count = -1
    pool_count = -1
    building_count = -1


def getCampingDetails():
    result = campingDetails
    result.camping_area = getArea()
    result.tree_count = treeCount()
    result.zone_count = zoneCount()
    result.emplacement_count = emplCount()
    result.pool_count = poolCount()
    result.building_count = buidCount()

    return result


emplacements = Emplacements.objects.all()


def getArea():
    total_area = 0
    for emp in emplacements:
        area_emp = emp.geom.area
        total_area += area_emp

    return total_area


def treeCount():
    arbres = Arbres.objects.all()
    return arbres.count()


def zoneCount():
    zone = ZoneCamping.objects.all()
    return zone.count()


def poolCount():
    pool = Piscines.objects.all()
    return pool.count()

def buidCount():
    build = Batiments.objects.all()
    return build.count()

def emplCount():
    return emplacements.count()


