from django.contrib.gis import admin
from models import Feedback
from models import CitySetting

class CityLocation(admin.OSMGeoAdmin):
    pass
    '''
    default_lon = 2407221.77716 
    default_lat = 9123608.26437
    default_zoom = 12
    '''
    
admin.site.register(Feedback)
admin.site.register(CitySetting, CityLocation)
