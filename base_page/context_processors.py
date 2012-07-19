"""
This file includes context processors
that is needed to render the base pages
"""
from models import CitySetting
from django.conf import settings

def city(request):
    try:
        city_settings = CitySetting.on_site.all()[0]
    except IndexError:
        city_settings = {}

    return {'city_settings': city_settings,
            'ANALYTICS_TEMPLATE': getattr(settings, 'ANALYTICS_TEMPLATE', 'analytics.js')}
