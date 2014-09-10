# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import contextlib
from django.utils.translation import activate, get_language


@contextlib.contextmanager
def language(code):
    """
    Activate given language
    """
    old_lang = get_language()
    activate(code)
    try:
        yield
    finally:
        activate(old_lang)
