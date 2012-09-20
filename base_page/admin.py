"""
Admin classes for base_page related models
"""
from django.contrib.gis import admin
from base_page.forms import OrganizationSettingForm
from base_page.models import Feedback
from base_page.models import OrganizationSetting
from django.conf import settings
from modeltranslation.admin import TranslationAdmin
    
class OrganizationSettingAdmin(TranslationAdmin, admin.OSMGeoAdmin):
    """
    The OrganizationSettingAdmin handles the organization specific settings
    for the site.
    """
    list_display = ('organization_name',
                    'title',
                    'blurb',
                    'provider',)
    
    default_lon = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_lon': 0})['default_lon']
    default_lat = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_lat': 0})['default_lat']
    default_zoom = getattr(settings,
                          'ORGANIZATION_ADMIN_DEFAULT_MAP_SETTINGS',
                          {'default_zoom': 4})['default_zoom']
    
    form = OrganizationSettingForm
   
admin.site.register(Feedback)
admin.site.register(OrganizationSetting, OrganizationSettingAdmin)
