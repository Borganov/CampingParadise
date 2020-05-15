from django.urls import path
from . import views

urlpatterns = [
    path('arbre/<int:gid>', views.arbre, name='arbre'),
    path('arbres.json', views.arbresjson, name='arbresjson'),
    path('arbres/', views.arbres, name='arbres'),
    path('emplacement/<int:gid>', views.emplacement, name='emplacement'),
    path('emplacements.json', views.emplacementsAlljson, name='emplacementsjson'),
    path('zones.json', views.zonesjson, name='zonesjson'),
    path('emplacements/<int:id>', views.emplacements, name='emplacements'),
    path('zones/<int:id>', views.zones, name='zones'),
    path('batiments.json', views.batimentsjson, name='batimentsjson'),
    path('batiments/', views.batiments, name='batiments'),
    path('piscines.json', views.piscinesjson, name='piscinesjson'),
    path('piscines/', views.piscines, name='piscines'),
    path('zoneCamping.json', views.zonecampingjson, name='zonecampingjson'),
    path('zoneCamping/', views.zonecamping, name='zonecamping'),
    path('accueil/', views.accueil, name='accueil')
]