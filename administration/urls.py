from django.urls import path
from . import views

urlpatterns = [
    path('arbre/<str:gid>', views.arbre, name='arbre'),
    path('arbres.json', views.arbresjson, name='arbresjson'),
    path('arbres/', views.arbres, name='arbres'),
    path('emplacement/<str:gid>', views.emplacement, name='emplacement'),
    path('emplacements.json', views.emplacementsjson, name='emplacementsjson'),
    path('emplacements/', views.arbres, name='emplacements')
]