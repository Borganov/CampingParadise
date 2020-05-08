from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import Arbres, Emplacements, Batiments, Piscines, ZoneCamping
from .util import emplacementDetails as ed
from .util import zonesDetails as zd
import json
from random import randint


# Create your views here.

def arbre(request, gid):
    arbres = Arbres.objects.filter(pk=gid)
    emplacements = Emplacements.objects.filter(pk=gid)
    return render(request, 'camping/arbre.html', {'arbreobj': arbres[0], 'emplacementobj': emplacements[0]})


def arbresjson(request):
    arbres = Arbres.objects.all()
    ser = serialize('geojson', arbres, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def arbres(request):
    context = {}
    return render(request, 'camping/arbres.html', context)


def emplacement(request, gid):
    emplacements = Emplacements.objects.filter(pk=gid)
    return render(request, 'camping/emplacement.html', {'emplacementobj': emplacements[0]})


def emplacementsAlljson(request):
    emplacements = Emplacements.objects.all()
    ser = serialize('geojson', emplacements, geometry_field='geom', fields=('gid', 'id', 'name', 'booked'))
    return HttpResponse(ser)


def zonesjson(request):
    zones = ZoneCamping.objects.all()
    ser = serialize('geojson', zones, geometry_field='geom', fields=('gid', 'id', 'name'))
    return HttpResponse(ser)


def emplacementdetails(request):
    emplacementdetails = ed.getEmplacementDetails(1)
    return render(request, 'camping/emplacement.html', {'emplacementobj': emplacementdetails[0]})


def emplacements(request, id):
    eff = ed.getEmplacementDetails(id)
    return render(request, 'camping/emplacements.html', {'emplacementobj': eff})


def zones(request, id):
    zone = zd.getZoneDetails(id)
    return render(request, 'camping/zones.html', {'zone': zone})


def batimentsjson(request):
    batiments = Batiments.objects.all()
    ser = serialize('geojson', batiments, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def batiments(request):
    context = {}
    return render(request, 'camping/batiments.html', context)

def piscinesjson(request):
    piscines = Piscines.objects.all()
    ser = serialize('geojson', piscines, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def piscines(request):
    context = {}
    return render(request, 'camping/piscines.html', context)


def zonecampingjson(request):
    zonecamping = ZoneCamping.objects.all()
    ser = serialize('geojson', zonecamping, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def zonecamping(request):
    context = {}
    return render(request, 'camping/zonecamping.html', context)


def admin(request):
    context = {}
    return render(request, 'camping/admin.html', context)
