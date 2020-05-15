from administration.models import Piscines, Arbres
from administration.models import Emplacements
from shapely.geometry import shape, Point
from django.core.serializers import serialize
import geopandas as gpd
from administration.models import Batiments


class emplacementDetails:
    tree_count = -1
    closest_swimmingpool_dist = -1
    closest_swimmingpool_name = "-"
    closest_building_dist = -1
    closest_building_name = "-"
    area = -1
    emp = -1
    booked = True


def getEmplacementById(idEmp):
    emplacements = Emplacements.objects.filter(gid=idEmp)
    emplacement = emplacements[0]
    return emplacement


def getEmplacementDetails(idEmp):
    result = emplacementDetails
    result.emp = getEmplacementById(idEmp)
    result.area = getArea(result.emp)
    result.tree_count = treeCount(result.emp)
    swimmingpool = distancepiscine(result.emp)
    result.closest_swimmingpool_dist = swimmingpool['dist']
    result.closest_swimmingpool_name = swimmingpool['name']
    building = distanceBuilding(result.emp)
    result.closest_building_dist = building['dist']
    result.closest_building_name = building['name']
    # result.closest_building_dist = distanceBuilding(result.emp)
    result.is_booked = getBookingStatus(result.emp)

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


def distancepiscine(emp):
    piscines = Piscines.objects.all()
    dist = 100000000000
    name = "-"
    em = emp.geom.centroid
    for p in piscines:
        point = p.geom.centroid
        dist_calc = em.distance(point)
        if dist_calc < dist:
            name = p.name
            dist = dist_calc

    return {"name": name, "dist": dist}


def distanceBuilding(emp):
    batiments = Batiments.objects.all()
    dist = 100000000000
    name = "-"
    em = emp.geom.centroid
    for b in batiments:
        point = b.geom.centroid
        dist_calc = em.distance(point)
        if dist_calc < dist:
            name = b.name
            dist = dist_calc

    return {"name": name, "dist": dist}


def getArea(emp):
    return emp.geom.area


def getBookingStatus(emp):
    booked = Emplacements.objects.filter(booked=False)
    booked = booked[0]
    return booked


def getBuildings():
    batiments = Batiments.objects.all()
    centroids = []
    for b in batiments:
        centroids.append(b.geom.centroid)
        print(b.geom.centroid)
        print(str(b.geom.centroid[0]) + ' ' + str(b.geom.centroid[1]))
    return centroids
