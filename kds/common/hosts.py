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

import nmap 
import netifaces


#TODO Validaciones

def get_active_hosts():

	default_gateway = netifaces.gateways().get('default').values()[0][0]

	nm = nmap.PortScanner()

	scan_result = nm.scan(default_gateway + "/24", None, '-sP')

	active_hosts = scan_result.get('scan').keys()

	if default_gateway in active_hosts:

		active_hosts.remove(default_gateway)

	return active_hosts