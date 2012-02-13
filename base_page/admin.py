from django.contrib import admin
from models import Feedback
from models import SiteSetting

class FeedbackAdmin(admin.ModelAdmin):
    pass

class SiteSettingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(SiteSetting, SiteSettingAdmin)
