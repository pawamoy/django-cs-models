# -*- coding: utf-8 -*-

"""Django Complex System Models package."""

from django.conf import settings

__version__ = '0.1.0'

COMPLEX_STRUCTURE = getattr(settings, 'COMPLEX_STRUCTURE', None)
COMPLEX_APP_NAME = getattr(settings, 'COMPLEX_APP_NAME', None)
