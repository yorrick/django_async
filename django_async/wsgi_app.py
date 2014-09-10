"""
WSGI config for django_async project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

from gevent import monkey
monkey.patch_all()

import os
from psycogreen.gevent import patch_psycopg


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_async.settings_prod")

patch_psycopg()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
