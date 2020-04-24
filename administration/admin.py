from django.contrib.gis import admin
from .models import Arbres, Batiments, Emplacements, Piscines, ZoneCamping
# Register your models here.

admin.site.register(Arbres, admin.OSMGeoAdmin)
admin.site.register(Batiments, admin.OSMGeoAdmin)
admin.site.register(Emplacements, admin.OSMGeoAdmin)
admin.site.register(Piscines, admin.OSMGeoAdmin)
admin.site.register(ZoneCamping, admin.OSMGeoAdmin),


