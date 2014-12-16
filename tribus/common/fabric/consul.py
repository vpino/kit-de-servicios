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

"""
This module contains directives to manage a Consul service

This module define funtions to accomplish the following tasks:

- Check if the Consul service is running
- Others 

.. versionadded:: 0.2
"""

# Importante considerar este planteamiento a futuro
# http://www.pythian.com/blog/loose-coupling-and-discovery-of-services-with-consul-part-1/

import os
import json
import requests
from tribus import BASEDIR
from tribus.common.utils import get_path
from tribus.common.logger import get_logger
from tribus.common.system import get_local_arch
from fabric.api import env, sudo, quiet
from tribus.common.recipes.recipe import RecipeDir
from tribus.config.base import CHARMSDIR, SERVICEDIR

log = get_logger()


def get_service_config(name):

	cfg = {}
	cfg['name'] = name
	cfg['img'] = "%s:test" % name
	comp_path = os.path.join(CHARMSDIR, name)
	cfg['path'] = comp_path
	with open(os.path.join(comp_path, 'config', 'app.json')) as f:
		data = f.read()
	j_data = json.loads(data)
	cfg['ports'] = '-p %s:%s' % (j_data['service']['port'], j_data['service']['port'])
	cfg['consul'] = env.docker_bridge

	return cfg


def docker_generate_service_base():
	"""
    Crea una imagen base de Consul

    .. versionadded:: 0.2
    """
	
	env.arch = get_local_arch()	
	if env.arch == 'i386':
		sudo('%(docker)s build -t service-base:test %(consul_dockerfile_i386)s' % env)
	elif env.arch == 'amd64':
		sudo('%(docker)s build -t service-base:test %(consul_dockerfile_amd64)s' % env)


def docker_check_service_base():
	"""
	Check if the consul image exists, build it if not.

	.. versionadded:: 0.2
	"""
	with quiet():
		log.info('Checking if we have a consul image ...')
		env.arch = get_local_arch()
		state = sudo('%(docker)s inspect service-base:test' % env)

	if state.return_code == 1:
		docker_generate_service_base()


def deploy_test_service():

	# Necesito asegurarme de que existe la imagen base para los servicios
	docker_check_service_base()

	# Debo asegurarme tambien de que el servicio de consul este corriendo en el host

	# Debe crearse una Excepcion 'Recipe Not Found'
	serv = RecipeDir(os.path.join(SERVICEDIR, env.service_name))

	components = serv.metadata.components.items()

	for n, name in components:

		cfg = get_service_config(name)
		
		comp_exists = sudo('docker inspect %(img)s' % cfg)

		if comp_exists.return_code == 1:
			sudo('docker build -t %(img)s %(path)s' % cfg)

		sudo('docker run -d %(ports)s -h %(name)s --name %(name)s %(img)s -join %(consul)s' % cfg)
