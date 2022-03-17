# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# create class
class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.IntegerField(default=0, blank=True, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(default=0.00, blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title

