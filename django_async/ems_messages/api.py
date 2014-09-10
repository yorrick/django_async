# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import logging
from django_async.utils import logged, apply_database_settings
from django_async.ems_messages.models import Message
from django.db import transaction


logger = logging.getLogger(__name__)


@logged(logger)
@transaction.atomic()
def save_message(message):
    """
    Saves a message in database
    """
    message.save()
    return message


@logged(logger)
def message_list(max = 5):
    """
    Returns a list of messages
    """
    query = Message.objects.order_by('-date')
    query = apply_database_settings(query)

    return list(query[:max])
