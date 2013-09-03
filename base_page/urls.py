from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('base_page.views',
            #test templates
            url(r'setlang/',
                'set_language',
                name='set_language'),
            url(r'feedback/',
                'feedback',
                name='feedback'),
            url(r'osmextra.js',
                'osmextra',
                name='osmextra'),
        )