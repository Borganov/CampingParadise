from administration.models import Piscines


class emplacementDetails:
    has_tree = False
    closest_swimmingpool_dist = 2.4
    closest_building_dist = 1.6
    area = 6.5


def getEmplacementDetails(idEmp):
    result = emplacementDetails
    result.has_tree = hasTree(idEmp)
    result.closest_building_dist = distanceBuilding(idEmp)
    result.area = getArea(idEmp)


def hasTree(idEmp):
    return True

def distancepiscine(idEmp):
    piscines = Piscines.objects.all()

def distanceBuilding(idEmp):
    pass

def getArea(idEmp):
    pass
