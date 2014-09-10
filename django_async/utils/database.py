# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.db.models.query import QuerySet


def apply_database_settings(query):
    """
    Applies different settings to the given query
    """
    assert isinstance(query, QuerySet), '{} object should be a query set'.format(query)

    if settings.SLOW_DB_QUERIES_BY > 0:
        # simulates a slow query with postgres
        query = query.extra(select={'sleep': "pg_sleep({})".format(settings.SLOW_DB_QUERIES_BY)})

    return query
