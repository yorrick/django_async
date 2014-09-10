# -*- coding: utf-8 -*-
# Developpement settings
from django_async.settings_common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ha+g0tl@5&z(*on(8^m86i^bi!j3-0#k^t#mszpx*ciat8r4qk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': '192.168.59.103',  # host of docker VM
        'PORT': 5432,
    }
}


ALLOWED_HOSTS = []

CACHES = {
    'default': {
#        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': 'unique-snowflake'
    }
}


SLOW_DB_QUERIES_BY = 0

