from django.urls import path
from . import views

urlpatterns = [
    path('arbre/<int:gid>', views.arbre, name='arbre'),
    path('arbres.json', views.arbresjson, name='arbresjson'),
    path('arbres/', views.arbres, name='arbres'),
    path('emplacement/<int:gid>', views.emplacement, name='emplacement'),
    path('emplacements.json', views.emplacementsAlljson, name='emplacementsjson'),
    path('emplacementsFree.json', views.emplacementsFreejson, name='emplacementsFreejson'),
    path('emplacementsBooked.json', views.emplacementsBookedjson, name='emplacementsBookedjson'),
    path('emplacements/<int:id>', views.emplacements, name='emplacements'),
    path('batiments.json', views.batimentsjson, name='batimentsjson'),
    path('batiments/', views.batiments, name='batiments'),
    path('piscines.json', views.piscinesjson, name='piscinesjson'),
    path('piscines/', views.piscines, name='piscines'),
    path('zoneCamping.json', views.zonecampingjson, name='zonecampingjson'),
    path('zoneCamping/', views.zonecamping, name='zonecamping'),
    path('admin/', views.admin, name='admin')
]