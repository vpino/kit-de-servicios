#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import djcelery
from celery.schedules import crontab
from kds import BASEDIR
from kds.common.utils import get_path
from kds.config.ldap import *

djcelery.setup_loader()

SITE_ID = 1

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['localhost']

ADMINS = ()
MANAGERS = ADMINS

USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'America/Caracas'
LANGUAGE_CODE = 'es'
DATABASE_OPTIONS = {'charset': 'utf8'}
DEFAULT_CHARSET = 'utf-8'
LOCALE_PATHS = [get_path([BASEDIR, 'kds', 'data', 'i18n'])]

SITE_ROOT = get_path([BASEDIR, 'kds', 'web'])
MEDIA_ROOT = ''
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = [get_path([BASEDIR, 'kds', 'data', 'static'])]
TEMPLATE_DIRS = [get_path([BASEDIR, 'kds', 'data', 'templates'])]

#DJANGO_STATIC = not DEBUG
#DJANGO_STATIC_MEDIA_ROOTS = [get_path([BASEDIR, 'kds', 'data'])]
#DJANGO_STATIC_FILENAME_GENERATOR = 'kds.common.utils.filename_generator'
#DJANGO_STATIC_NAME_MAX_LENGTH = 200

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'kds.web.urls'
WSGI_APPLICATION = 'kds.web.wsgi.application'

# This should be secret, but as we are in development, doesn't matter
# Production settings should be set in kds/config/web_production.py
# Other local configuration should be set in kds/config/web_local.py
SECRET_KEY = 'oue0893ro5c^82!zke^ypu16v0u&%s($lnegf^7-vcgc^$e&$f'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASEDIR, 'db.sqlite3'),
    }
}

APPEND_SLASH = True
TASTYPIE_ALLOW_MISSING_SLASH = True
TASTYPIE_FULL_DEBUG = False
API_LIMIT_PER_PAGE = 20
TASTYPIE_DEFAULT_FORMATS = ['json']
ACCOUNT_ACTIVATION_DAYS = 7

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kombu.transport.django',
    'djcelery',
    'tastypie',
    'kds.web',
    'kds.web.kit',
    'kds.web.api',
)

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'waffle.middleware.WaffleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.tz',
    'kds.web.processors.default_context',
)

try:
    from kds.config.logger import *
except:
    pass

try:
    from kds.config.web_local import *
except:
    pass

try:
    from kds.config.web_production import *
except:
    pass
