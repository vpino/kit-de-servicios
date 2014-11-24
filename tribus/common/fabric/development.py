#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013-2014 Tribus Developers
#
# This file is part of Tribus.
#
# Tribus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tribus is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import json
import time
from tribus import BASEDIR
from contextlib import nested
from tribus.common.utils import get_path
from tribus.common.logger import get_logger
from fabric.api import run, env, settings, sudo, hide, put, cd


log = get_logger()

def deploy_test_service():
    """
    Este metodo despliega un servicio.

    Premisa #1: Por cada componente se crea la imagen y se
    inicia el contenedor.
    
    Secuencia de despliegue para mediawiki:

    - Construir imagen del servidor de consul
    - Arrancar imagen del servidor de consul
    - Construir la imagen de mysql
    - Arrancar la imagen de mysql
    - Crear la imagen de mediawiki
    - Arrancar la imagen de mediawiki

    .. versionadded:: 0.2
    """

    env.port = 22
    env.short_name = 'wiki'
    env.long_name = 'Wiki MPPAT'
    
    components = {
        1 : {'name' : 'mysql',
             'role' : 'db',
             'imgname' : 'mysql:test',
             'ports' : '-p 3306:3306',
             'dockerfile' : get_path([BASEDIR, 'tribus', 'data',
             'charms', 'mysql'])
        },

        2 : {'name' : 'mediawiki',
             'imgname' : 'mediawiki:test',
             'ports' : '-p 80:80',
             'dockerfile' : get_path([BASEDIR, 'tribus', 'data',
             'charms', 'mediawiki'])
        },
    }

    consul_server = {
        'name' : 'consul-server',
        'imgname' : 'consul-server:test',
        'ports': '-p 8300:8300 -p 8301:8301 -p 8301:8301/udp '\
                 '-p 8302:8302 -p 8302:8302/udp -p 8400:8400 '\
                 '-p 8500:8500 -p 8600:53/udp',
        'dockerfile' : get_path([BASEDIR, 'tribus', 'data', 'consul'])
    }

    with hide('warnings', 'stderr', 'running'):
        # Verificar si existe una imagen de consul en la mauqina 
        # donde se hara el despliegue
        consul_exists = sudo('docker inspect %(imgname)s ' % consul_server)

        if consul_exists.return_code == 1:
            # No existe la imagen, procedemos a crearla
            sudo('docker build -t %(imgname)s '\
                 '%(dockerfile)s' % consul_server)
        elif consul_exists.return_code > 1:
            print "No se ha podido iniciar consul"
            print consul_exists.return_code
            return
        
        # Si la imagen existe, arrancamos el contenedor
        sudo('docker run -d %(ports)s '
             '-h %(name)s --name %(name)s '
             '%(imgname)s -server -bootstrap' % consul_server)
        
        # Obtener la IP del servidor de consul
        consul_addr = sudo('%(docker)s inspect -f '
                           '"{{.NetworkSettings.IPAddress}}" '
                           'consul-server ' % env)

        for n, component in components.items():
            comp_exists = sudo('docker inspect %(imgname)s ' % component)

            if comp_exists.return_code == 1:
                sudo('docker build -t %(imgname)s '
                    '%(dockerfile)s' % component)

            component['join_addr'] = consul_addr
            
            sudo('docker run -d %(ports)s '
                 '-h %(name)s --name %(name)s '
                 '%(imgname)s -join %(join_addr)s ' % component)
