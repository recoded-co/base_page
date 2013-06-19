"""
This file includes context processors
that is needed to render the base pages
"""
from base_page.models import OrganizationSetting
from django.conf import settings

def organization(request):
    """
    This context processor adds variables used in all pages
    that is made based on the base_page app
    """
    try:
        org_settings = OrganizationSetting.on_site.all()[0]
    except IndexError:
        org_settings = {}

    return {'org_settings': org_settings,
            'ANALYTICS_TEMPLATE': getattr(settings,
                                          'ANALYTICS_TEMPLATE',
                                          'analytics.js'),
            'USER_REGISTRATION_ENABLED': getattr(settings,
                                          'USER_REGISTRATION_ENABLED',
                                          False),
            'LOGO_FILENAME': getattr(settings,
                                          'LOGO_FILENAME',
                                          ''),
            }
