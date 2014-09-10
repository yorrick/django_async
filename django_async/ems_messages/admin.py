# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from django_async.ems_messages.models import Message


admin.site.register(Message)

