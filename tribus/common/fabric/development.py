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
from tribus import BASEDIR
from contextlib import nested
from tribus.common.utils import get_path
from tribus.common.logger import get_logger
from fabric.api import run, env, settings, sudo, hide, put, cd

log = get_logger()


def docker_kill_dev_containers():
    """
    Destroy all devel containers listed with ``docker ps -aq``.

    .. versionadded:: 0.2
    """

    env.port = 22

    with hide('warnings', 'stderr', 'running', 'stdout'):

        log.info('Listing development containers ...')
        # Elimino los caracteres \r \n para dejar 
        # solo los hash de los contendores
        # Hay que hacer un test de lo que bota docker.io ps -aq
        containers = sudo('%(docker)s ps -aq' % env).split("\r\n")

        for container in containers:
            cont = sudo('%s inspect %s' % (env.docker, container))
            if cont.return_code == 0:
                jcont = json.loads(cont)
                if 'dev' in jcont[0]['Name']:
                    log.info('Deleting containers %s ...' % container)
                    sudo('%s stop --time 1 %s' % (env.docker, container))
                    sudo('%s rm -fv %s' % (env.docker, container))


def docker_kill_dev_images():
    """
    Destroy all devel images listed with ``docker images -q``.

    .. versionadded:: 0.2
    """

    env.port = 22

    with hide('warnings', 'stderr', 'running', 'stdout'):

        log.info('Listing development images ...')
        
        images = sudo('%(docker)s images -q' % env).split("\r\n")
        
        for image in images:
            cont = sudo('%s inspect %s' % (env.docker, image))
            if cont.return_code == 0:
                jimg = json.loads(cont)
                if ":" in jimg[0]['ContainerConfig']['Image']:
                    img_name, tag = jimg[0]['ContainerConfig']['Image'].split(":")
                    if tag == "dev":
                        log.info('Deleting image %s ...' % image)
                        sudo('%s rmi -f %s' % (env.docker, image))


def docker_create_service_cluster():
    """
    Crea un cluster de consul para un servicio.

    .. versionadded:: 0.2
    """

    env.port = 22
    env.target_img = "consul:test"
    env.build_dockerfile = get_path([BASEDIR, 'tribus', 'data', 'consul'])

    with hide('warnings', 'stderr', 'running'):
        # Deben agregarse algunas verificaciones previas
        # por ejemplo, debe existir la imagen base para los 
        # nodos, de lo contrario debe crearse

        # - Necesito asignar un nombre a la imagen
        # - Necesito especificar de donde se construye la imagen

        # Para no ralentizar mas el desarrollo, generare la imagen a partir
        # de un Dockerfile a pesar de que pueden existir otras tecnicas 
        # mas eficientes para generar las imagenes.

        bimage = sudo('%(docker)s build -t %(target_img)s %(build_dockerfile)s' % env)


def create_component_image():
    """
    Crea una imagen de un componente de un servicio.

    Para crear un componente necesito el nombre del componente.

    Para construir la imagen de los componentes utilizare dockerfiles
    ubicados en el directorio correspondiente a cada charm.

    .. versionadded:: 0.2
    """

    env.port = 22
    #env.comp_name = 'mysql'
    env.comp_name = 'mediawiki'
    env.df_path = get_path([BASEDIR, 'tribus', 'data', 'charms', env.comp_name])

    with hide('warnings', 'stderr', 'running'):

        base_exists = sudo('%(docker)s inspect consul:test' % env)

        if base_exists.return_code == 0:
            cimage = sudo('%(docker)s build -t %(comp_name)s:test %(df_path)s' % env)


def deploy_service():
    """
    Crea la infraestructura necesaria para un servicio.
    En esta funcion debe estar la secuencia a seguir para conectar
    los componentes de un servicio entre si e iniciarlo.

    Aqui necesito una lista de los componentes que integran este servicio.
    
    .. versionadded:: 0.2
    """

    with hide('warnings', 'stderr', 'running'):

        base_exists = sudo('%(docker)s inspect %(charm_name)s-base:base' % env)


def start_service():
    """
    Inicia los componentes de un servicio.
    
    .. versionadded:: 0.2
    """

    env.port = 22
    env.serv_name = 'servicioA'
    env.comp_list = ['mysql']
    env.cluster_ports = '-p 8300:8300 -p 8301:8301 -p 8301:8301/udp '\
    '-p 8302:8302 -p 8302:8302/udp -p 8400:8400 -p 8500:8500 -p 8600:53/udp'

    # Los puertos que utiliza el servicio se deben obtener a traves de
    # alguna configuracion externa

    with hide('warnings', 'stderr', 'running'):

        rc = sudo('%(docker)s run -d %(cluster_ports)s '
                  '-h %(serv_name)s-server --name %(serv_name)s-server ' # -v /data:/data
                  'consul:test -server -bootstrap' % env)

        if rc.return_code == 0:
            env.join_ip = sudo('%(docker)s inspect -f '
                     '"{{.NetworkSettings.IPAddress}}" '
                     '%(serv_name)s-server ' % env)

            for comp in env.comp_list:
                env.comp = comp
                sudo('%(docker)s run -d -p 3306:3306 '
                     '-h %(comp)s --name %(comp)s ' # -v /data:/data
                     '%(comp)s:test -join %(join_ip)s' % env)
        
