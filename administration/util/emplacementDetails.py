from administration.models import Piscines
from administration.models import Emplacements
from django.core.serializers import serialize
import geopandas as gpd
from administration.models import Batiments


class emplacementDetails:
    has_tree = False
    closest_swimmingpool_dist = 2.4
    closest_swimmingpool_id = 2
    closest_building_dist = 1.6
    closest_building_id = 1
    area = 6.5


def getEmplacementDetails(idEmp):
    result = emplacementDetails
    result.has_tree = hasTree(idEmp)
    result.closest_building_dist = distanceBuilding(idEmp)
    result.area = getArea(idEmp)


def hasTree(idEmp):
    return 'emplacement.id.toString()'


def distancepiscine(idEmp):
    piscines = Piscines.objects.all()

    return False


def distanceBuilding(idEmp):
    pass


def getArea(idEmp):
    """
     emplacements = Emplacements.objects.filter(pk=idEmp).values()
    test = emplacements[0]['geom'].json
    truc = gpd.read_file(test)
    print(test)
    print(truc.crs)
    print(truc.area)
    print(truc.bounds)
    truc = truc.to_crs({'init': 'epsg:3857'})
    print(truc.crs)
    print(truc.area)
    print(truc.bounds)
    :param idEmp:
    :return:
    """
    emplacements = Emplacements.objects.filter(pk=idEmp)
    emplacement = emplacements[0]
    print(emplacement.geom.area)
    print(emplacement.geom.boundary)




