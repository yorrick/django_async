import logging
from django_async.ems_messages.utils import logged
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



