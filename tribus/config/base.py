#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tribus import BASEDIR
from tribus.common.utils import get_path

NAME = u'Kit de servicios'
VERSION = (0, 1, 0, 'alpha', 1)
URL = u'http://github.com/tribusdev/kit-servicios'
AUTHOR = u'Desarrolladores de Tribus'
AUTHOR_EMAIL = u'tribusdev@googlegroups.com'
DESCRIPTION = (u'Automatización y despliegue de servicios para la AP.')
LICENSE = u'GPL'

if BASEDIR == '/usr/share/pyshared':
    CONFDIR = '/etc/tribus'
    BINDIR = '/usr/bin'
    SHAREDIR = '/usr/share/tribus'
    DOCDIR = '/usr/share/doc/tribus'
    ICONDIR = '/usr/share/icons/hicolor'
    LOCALEDIR = '/usr/share/locale'
    PACKAGECACHE = '/var/cache/tribus'
    CHARMSDIR = BASEDIR + '/tribus/data/charms'
    SERVICEDIR = BASEDIR + '/tribus/data/services'

else:
    CONFDIR = BASEDIR + '/tribus/config'
    BINDIR = BASEDIR
    SHAREDIR = BASEDIR
    DOCDIR = BASEDIR + '/tribus/data/docs'
    LOCALEDIR = BASEDIR + '/tribus/i18n'
    ICONDIR = BASEDIR + '/tribus/data/icons'
    PACKAGECACHE = BASEDIR + '/packagecache'
    CHARMSDIR = BASEDIR + '/tribus/data/charms'
    SERVICEDIR = BASEDIR + '/tribus/data/services'

