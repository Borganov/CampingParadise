from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from administration.models import Arbres


def arbres(request):
    list_arbres = Arbres.objects.order_by('-gid')[:3]
    output = ([a.geom for a in list_arbres])
    return HttpResponse(output)

