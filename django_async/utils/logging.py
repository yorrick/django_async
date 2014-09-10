# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from decorator import decorator


def logged(the_logger):
    """
    Protects a view if given product is not activated
    """
    @decorator
    def internal_decorator(func, *args, **kwargs):
        the_logger.debug('Calling function {} with parameters {} {}'.format(func, args, kwargs))
        result = func(*args, **kwargs)
        the_logger.debug('Function result: {}'.format(result))
        return result

    return internal_decorator
