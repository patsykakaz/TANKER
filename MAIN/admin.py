#-*- coding: utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage
from .models import *

# Press_fieldsets = deepcopy(PageAdmin.fieldsets)
# Press_fieldsets[0][1]["fields"].insert(-1, "baseline")
class PressReleaseInline(admin.TabularInline):
    model = PressReleaseCaption
    extra = 5
class PublicationInline(admin.TabularInline):
    model = PublicationCaption
    extra = 5
class PressAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets)
    inlines = (PressReleaseInline,PublicationInline)

Job_fieldsets = deepcopy(PageAdmin.fieldsets)
Job_fieldsets[0][1]["fields"].insert(-1, "job_type")
Job_fieldsets[0][1]["fields"].insert(-1, "description_job")
class JobAdmin(PageAdmin):
    fieldsets = Job_fieldsets


admin.site.register(Press, PressAdmin)
admin.site.register(Job, JobAdmin)


