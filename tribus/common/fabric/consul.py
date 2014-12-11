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


- Create a Consul server if needed
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

log = get_logger()

env.consul_container = "consul-server"
env.consul_image = "consul-server"
env.consul_ports = '-p 8300:8300 -p 8301:8301 -p 8301:8301/udp '\
             	   '-p 8302:8302 -p 8302:8302/udp -p 8400:8400 '\
                   '-p 8500:8500 -p 8600:53/udp'

env.consul_dockerfile_i386 = get_path([BASEDIR, 'tribus', 'data', 'consul', 'i386'])
env.consul_dockerfile_amd64 = get_path([BASEDIR, 'tribus', 'data', 'consul', 'amd64'])
env.components = {
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


def docker_generate_consul_base_image():
    """
    Crea una imagen base de Consul

    .. versionadded:: 0.2
    """

    env.arch = get_local_arch()
    if env.arch == 'i386':
    	sudo('%(docker)s build -t %(consul_image)s-%(arch)s:test %(consul_dockerfile_i386)s' % env)
    elif env.arch == 'amd64':
    	sudo('%(docker)s build -t %(consul_image)s-%(arch)s:test %(consul_dockerfile_amd64)s' % env)
    

def docker_check_consul_image():
	"""
	Check if the consul image exists, build it if not.

	.. versionadded:: 0.2
	"""
	with quiet():
		log.info('Checking if we have a consul image ...')
		env.arch = get_local_arch()
		state = sudo('%(docker)s inspect %(consul_image)s-%(arch)s:test' % env)

	if state.return_code == 1:
		docker_generate_consul_base_image()


def docker_start_consul():
	"""
	Starts the consul container.

	.. versionadded:: 0.2
	"""

	docker_check_consul_image()

	log.info('Starting Consul service ...')

	env.arch = get_local_arch()

	with quiet():

		log.info('Checking if the Consul container is up ...')

		state = sudo('%(docker)s inspect %(consul_container)s' % env)

		if state.return_code == 0:
			output = json.loads(state.stdout)

			if not output[0]['State']['Running']:
				sudo('%(docker)s rm -f %(consul_container)s' %  env)
			 	sudo('%(docker)s run -d %(consul_ports)s '
		     	 '-h %(consul_container)s --name %(consul_container)s '
		     	 '%(consul_image)s-%(arch)s:test -server -bootstrap ' % env)
			 	log.info('Consul esta corriendo en http://localhost:8500')
			else:
				log.info('Consul ya esta corriendo en http://localhost:8500')			 	

		elif state.return_code == 1:
			sudo('%(docker)s run -d %(consul_ports)s '
		     	 '-h %(consul_container)s --name %(consul_container)s '
		     	 '%(consul_image)s-%(arch)s:test -server -bootstrap ' % env)

			log.info('Consul esta corriendo en http://localhost:8500')


def deploy_test_service():

	docker_start_consul()

	consul_addr = sudo('%(docker)s inspect -f '
                       '"{{.NetworkSettings.IPAddress}}" '
                       'consul-server ' % env)

	for n, component in env.components.items():
            comp_exists = sudo('docker inspect %(imgname)s ' % component)

            if comp_exists.return_code == 1:
                sudo('docker build -t %(imgname)s '
                    '%(dockerfile)s' % component)

            component['join_addr'] = consul_addr
            
            sudo('docker run -d %(ports)s '
                 '-h %(name)s --name %(name)s '
                 '%(imgname)s -join %(join_addr)s ' % component)


def consul_query_status():

	with quiet():
		consul_addr = sudo('%(docker)s inspect -f '
	                       '"{{.NetworkSettings.IPAddress}}" '
	                       'consul-server ' % env)

		consul_health = "http://%s:8500/v1/health/node" % (consul_addr)

		consul_node = os.path.join(consul_health, "consul-server")

		response = requests.get(consul_node).json()

		if response:
			if response[0]['Status'] == "passing":
				return (True, response[0]['Output'])
			else:
				return (False, response[0]['Output'])


def consul_query_services():
	with quiet():
		consul_addr = sudo('%(docker)s inspect -f '
	                       '"{{.NetworkSettings.IPAddress}}" '
	                       'consul-server ' % env)

		consul_services = "http://%s:8500/v1/catalog/services" % (consul_addr)

		response = requests.get(consul_services).json()

		if response:
			return response
