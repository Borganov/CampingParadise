from django.urls import path
from . import views

urlpatterns = [

    path('arbres.json', views.arbresjson, name='arbresjson'),
    path('emplacements.json', views.emplacementsAlljson, name='emplacementsjson'),
    path('zones.json', views.zonesjson, name='zonesjson'),
    path('emplacements/<int:id>', views.emplacements, name='emplacements'),
    path('zones/<int:id>', views.zones, name='zones'),
    path('batiments.json', views.batimentsjson, name='batimentsjson'),
    path('piscines.json', views.piscinesjson, name='piscinesjson'),
    path('zoneCamping.json', views.zonecampingjson, name='zonecampingjson'),
    path('accueil/', views.accueil, name='accueil')
]