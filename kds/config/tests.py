#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kds import BASEDIR
from kds.common.utils import get_path
from kds.config.ldap import AUTH_LDAP_BASE

DEBUG = True

SITE_ROOT = get_path([BASEDIR, 'kds', 'web'])
MEDIA_ROOT = ''
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = [get_path([BASEDIR, 'kds', 'data', 'static'])]
TEMPLATE_DIRS = [get_path([BASEDIR, 'kds', 'data', 'templates'])]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_auth_ldap',
    'django_static',
    'kds.web.cloud',
    'south',
    'haystack',
    #'waffle',
)

ROOT_URLCONF = 'kds.web.urls'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
