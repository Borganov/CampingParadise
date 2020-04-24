from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import Arbres
# Create your views here.


def arbresjson(request):
    arbres = Arbres.objects.all()
    ser = serialize('geojson', arbres, geometry_field='geom', fields=('gid',))
    return HttpResponse(ser)


def arbres(request):
    context ={ }
    return render(request, 'templates/camping/arbres.html', context)
