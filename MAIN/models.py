#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.models import upload_to



class Job(Page,RichText):
    job_type = models.CharField(null=False, blank=False, verbose_name='Type d\'emploi', max_length=255)
    description_job = RichTextField()

    def save(self, *args, **kwargs):
        self.in_menus = []
        try: 
            self.parent = Page.objects.get(title='JOBS')
        except: 
            pass
        super(Job, self).save(*args, **kwargs)

class Press(Page):
    # middleBackgroundColor = ColorField()
    pass
class PressReleaseCaption(models.Model):
    master = models.ForeignKey("Press")
    title = models.CharField(max_length=255, null=False, blank=False)
    lien_PDF = models.FileField(upload_to='press/', null=False, blank=False)
    date = models.DateField(null=False, blank=False)

class PublicationCaption(models.Model):
    master = models.ForeignKey("Press")
    title = models.CharField(max_length=255, null=False, blank=False)
    illustration = FileField(verbose_name=_("Illustration"),
        upload_to=upload_to("MAIN.PublicationCaption.illustration", "Publication"),
        format="Image", max_length=255)
    lien = models.URLField(null=False, blank=True)







