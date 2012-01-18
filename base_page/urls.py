from django.conf import settings
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('base_page.views',
            #test templates
            url(r'^setlang/',
                'set_language',
                name='set_language'),
            url(r'^feedback/',
                'feedback',
                name='feedback'),
        )


if getattr(settings, 'DEBUG', False):
    urlpatterns += patterns('base_page.views',
            (r'^template/(\w+)', 'test'),
        )