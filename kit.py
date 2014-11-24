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

import optparse
from tribus.common.fabric.consul import docker_start_consul


def main():
    """Runs program and handles command line options"""

    p = optparse.OptionParser(description='Interfaz para el kit de servicios',
                              prog='kitservicios',
                              version='kitservicios 0.1',
                              usage='%prog [servicios or equipos]')
    options, arguments = p.parse_args()

    if len(arguments) == 1:

    	if arguments[0] == 'init':
            docker_start_consul()
 		
    	elif arguments[0] == 'servicios':
    		values = servicios()
    		print values
    	else:
    		p.print_help()
    else:
    		p.print_help()

if __name__ == '__main__':
	main()