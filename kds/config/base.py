#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Canaima GNU/Linux
#
# This file is part of KDS.
#
# KDS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# KDS is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from kds import BASEDIR
from kds.common.utils import get_path

NAME = u'Kit de servicios'
VERSION = (0, 1, 0, 'alpha', 1)
URL = u''
AUTHOR = u'Desarrolladores de Canaima GNU/Linux'
AUTHOR_EMAIL = u''
DESCRIPTION = (u'Automatización y despliegue de servicios para la AP.')
LICENSE = u'GPL'

if BASEDIR == '/usr/share/pyshared':
    CONFDIR = '/etc/kds'
    BINDIR = '/usr/bin'
    SHAREDIR = '/usr/share/kds'
    DOCDIR = '/usr/share/doc/kds'
    ICONDIR = '/usr/share/icons/hicolor'
    LOCALEDIR = '/usr/share/locale'
    PACKAGECACHE = '/var/cache/kds'
    CHARMSDIR = BASEDIR + '/kds/data/charms'
    ROLESDIR = BASEDIR + '/kds/data/roles'
    SERVICEDIR = BASEDIR + '/kds/data/services'

else:
    CONFDIR = BASEDIR + '/kds/config'
    BINDIR = BASEDIR
    SHAREDIR = BASEDIR
    DOCDIR = BASEDIR + '/kds/data/docs'
    LOCALEDIR = BASEDIR + '/kds/i18n'
    ICONDIR = BASEDIR + '/kds/data/icons'
    PACKAGECACHE = BASEDIR + '/packagecache'
    CHARMSDIR = BASEDIR + '/kds/data/charms'
    ROLESDIR = BASEDIR + '/kds/data/roles'
    SERVICEDIR = BASEDIR + '/kds/data/services'

