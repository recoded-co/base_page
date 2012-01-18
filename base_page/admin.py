from django.contrib import admin
from models import Feedback
from models import SiteSettings

class FeedbackAdmin(admin.ModelAdmin):
    pass

class SiteSettingsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)