# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import djangoClasses

# registering model
admin.site.register(djangoClasses)
