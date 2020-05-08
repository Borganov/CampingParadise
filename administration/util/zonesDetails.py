from administration.models import ZoneCamping, Emplacements

class zonesDetails:
    zone = "-"
    area = -1
    emp_count = -1
    area_rate = -1

def getZoneById(idZone):
    zones = ZoneCamping.objects.filter(gid=idZone)
    zone = zones[0]
    return zone

def getZoneDetails(idZone):
    result = zonesDetails
    result.zone = getZoneById(idZone)
    result.area = result.zone.geom.area
    result.emp_count = emplacementsCount(result.zone)
    result.area_rate = areaRate(result.zone)
    return result

def emplacementsCount(zone):
    emplacements = Emplacements.objects.all()
    count = 0
    polygon = zone.geom
    for emp in emplacements:
        point = emp.geom.centroid
        if polygon.contains(point):
            count += 1
    return count

def areaRate(zone):
    zones = ZoneCamping.objects.all()
    area_tot = 0
    for z in zones:
        area_tot += z.geom.area

    area_zone = zone.geom.area

    result = area_zone*100/area_tot
    return result