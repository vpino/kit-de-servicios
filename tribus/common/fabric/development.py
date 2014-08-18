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
from contextlib import nested
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
