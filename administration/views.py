from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import Arbres, Emplacements
# Create your views here.


def arbresjson(request):
    arbres = Arbres.objects.all()
    ser = serialize('geojson', arbres, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def arbres(request):
    context ={ }
    return render(request, 'camping/arbres.html', context)


def emplacementsjson(request):
    emplacements = Emplacements.objects.all()
    ser = serialize('geojson', emplacements, geometry_field='geom', fields=('gid', 'id'))
    return HttpResponse(ser)


def emplacements(request):
    context ={ }
    return render(request, 'camping/emplacements.html', context)
