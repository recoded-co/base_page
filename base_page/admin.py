from django.contrib.gis import admin
from models import Feedback
from models import CitySetting
from django.conf import settings
    
class CityLocation(admin.OSMGeoAdmin):
    default_lon = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_lon': 0})['default_lon']
    default_lat = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_lat': 0})['default_lat']
    default_zoom = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_zoom': 4})['default_zoom']
   
admin.site.register(Feedback)
admin.site.register(CitySetting, CityLocation)
