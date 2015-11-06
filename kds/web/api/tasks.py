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

from celery import task
from kds.ansible import deploy_service

@task
def saludar(*args):
    print "Hola esto es un saludo!"


@task
def queue_service_deploy(*args): 

    config = args[0].get('config', None)

    username = config.get('username', None)
    passwd = config.get('passwd', None)
    ipadd = config.get('ipadd', None)

    extras = {}
    for campo in config.get('campos'):
        extras[campo['field_name']] = campo['default']

    hosts = []

    if ipadd:
    	hosts.append(ipadd)

    deploy_service(username, passwd, hosts, extras)
