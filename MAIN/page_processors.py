#-*- coding: utf-8 -*-
from __future__ import unicode_literals

# import random
# secure_random = random.SystemRandom()

# from django.db.models import Q
# from django.http import HttpResponse, HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from mezzanine.blog.models import *
from MAIN.models import *

@processor_for("press")
def processor_section(request, page):
    master = Press.objects.last()
    PressRelease_all = PressReleaseCaption.objects.filter(master=master)
    Publication_all = PublicationCaption.objects.filter(master=master)
    return locals()

@processor_for("jobs")
def processor_section(request, page):
    Jobs = Job.objects.all()
    return locals()




