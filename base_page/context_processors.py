"""
This file includes context processors
that is needed to render the base pages
"""
from models import CitySetting

def city_context(request):
    try:
        city_settings = CitySetting.on_site.all()[0]
    except IndexError:
        city_settings = {}

    return {'city_settings': city_settings}
