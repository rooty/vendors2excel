# -*- coding: utf-8 -*-
__author__ = 'rooty'

import os
import django
# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = (os.path.join(os.path.dirname(__file__), '..').replace('\\','/'),)


