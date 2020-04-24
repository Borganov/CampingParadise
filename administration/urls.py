from django.urls import path
from . import views

urlpatterns = [
    path('arbres.json', views.arbresjson, name='arbresjson'),
    path('arbres/', views.arbres, name='arbres'),
    path('emplacements.json', views.arbresjson, name='emplacementsjson'),
    path('emplacements/', views.arbres, name='emplacements')
]