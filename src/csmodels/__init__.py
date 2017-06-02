# -*- coding: utf-8 -*-

"""Django Complex System Models package."""

from django.conf import settings

COMPLEX_STRUCTURE = getattr(settings, 'COMPLEX_STRUCTURE', None)
COMPLEX_APP_NAME = getattr(settings, 'COMPLEX_APP_NAME', None)
