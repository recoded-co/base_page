from django.contrib.sites.models import Site
from django.contrib.gis.db import models as geomodel
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.managers import CurrentSiteManager

class Feedback(models.Model):
    """
    This model stores all the feedback
    given for the softGIS django application.

    When a feedback is saved it sends an email
    to the administrators as set in settings.py.

    >>> from django.conf import settings
    >>> from base_page.models import Feedback
    >>> from django.contrib.sites.models import Site
    >>> from django.core import mail
    >>> fb = Feedback(content='some feedback',site=Site.objects.get_current())
    >>> fb.save()
    >>> mail.outbox[0].body
    'some feedback'
    """
    site = models.ForeignKey(Site)
    content = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if self.content != "":
            send_mail('Feedback for the softGIS application',
                    self.content,
                    'do-not-reply@pehmogis.fi',
                    [admin[1] for admin in settings.ADMINS],
                    fail_silently=True)

            super(Feedback, self).save(*args, **kwargs)
        else:
            pass

    def __unicode__(self):
        return u"feedback " + str(self.create_time)


class CitySetting(models.Model):
    site = models.ForeignKey(Site,
                             unique = True,
                             default = getattr(settings,
                                               'SITE_ID',
                                               1),
                             editable = False)
    city_name = models.CharField(max_length = 30,
                                 default = 'City')
    background_color = models.CharField(max_length = 7,
                                        default = '#e8ae6a')
    text_color = models.CharField(max_length = 7,
                                  default = '#e8ae6a')
    title = models.CharField(max_length = 50,
                             default = 'test page')
    blurb = models.CharField(max_length = 50,
                             default = 'Help us improve our City')
    provider = models.CharField(max_length = 30,
                                default = 'Geonition')
    provider_url = models.URLField()
    city_area = geomodel.PolygonField(srid = getattr(settings,
                                                     'SPATIAL_REFERENCE_SYSTEM_ID',
                                                     4326))
    on_site = CurrentSiteManager()


    def __unicode__(self):
        return u"%s" % (self.site.name,)
