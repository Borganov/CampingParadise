from administration.models import Piscines, Arbres
from administration.models import Emplacements
from shapely.geometry import shape, Point
from django.core.serializers import serialize
import geopandas as gpd
from administration.models import Batiments


class emplacementDetails:
    tree_count = -1
    closest_swimmingpool_dist = -1
    closest_swimmingpool_id = -1
    closest_building_dist = -1
    closest_building_id = -1
    area = -1
    emp = -1


def getEmplacementById(idEmp):
    emplacements = Emplacements.objects.filter(gid=idEmp)
    emplacement = emplacements[0]
    return emplacement


def getEmplacementDetails(idEmp):
    result = emplacementDetails
    result.emp = getEmplacementById(idEmp)
    result.area = getArea(result.emp)
    result.tree_count = treeCount(result.emp)
    #result.closest_building_dist = distanceBuilding(idEmp)

    return result


def treeCount(emp):
    arbres = Arbres.objects.all()
    count = 0
    polygon = emp.geom
    for a in arbres:
        point = a.geom
        if polygon.contains(point):
            count += 1
    return count




def distancepiscine(idEmp):
    piscines = Piscines.objects.all()

    return False


def distanceBuilding(idEmp):
    pass


def getArea(emp):
    return emp.geom.area




