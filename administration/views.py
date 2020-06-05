from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import Arbres, Emplacements, Batiments, Piscines, ZoneCamping
from .util import emplacementDetails as ed
from .util import zonesDetails as zd
from .util import campingDetails as cd
import json
from random import randint


# Create your views here.

def arbresjson(request):
    arbres = Arbres.objects.all()
    ser = serialize('geojson', arbres, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def emplacements(request, id):
    eff = ed.getEmplacementDetails(id)
    return render(request, 'camping/emplacements.html', {'emplacementobj': eff})


def emplacementsAlljson(request):
    emplacements = Emplacements.objects.all()
    ser = serialize('geojson', emplacements, geometry_field='geom', fields=('gid', 'id', 'name', 'booked'))
    return HttpResponse(ser)


def zonesjson(request):
    zones = ZoneCamping.objects.all()
    ser = serialize('geojson', zones, geometry_field='geom', fields=('gid', 'id', 'name'))
    return HttpResponse(ser)


def zones(request, id):
    zone = zd.getZoneDetails(id)
    return render(request, 'camping/zones.html', {'zone': zone})


def batimentsjson(request):
    batiments = Batiments.objects.all()
    ser = serialize('geojson', batiments, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def piscinesjson(request):
    piscines = Piscines.objects.all()
    ser = serialize('geojson', piscines, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def zonecampingjson(request):
    zonecamping = ZoneCamping.objects.all()
    ser = serialize('geojson', zonecamping, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def accueil(request):
    cff = cd.getCampingDetails()
    return render(request, 'camping/accueil.html', {'campingobj': cff})
