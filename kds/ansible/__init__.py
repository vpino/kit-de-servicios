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

import os

from kds.common.logger import get_logger
from kds.config.base import ROLESDIR

from ansible import utils
from ansible import callbacks
from ansible.playbook import PlayBook

log = get_logger()

stats = callbacks.AggregateStats()
playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)


def deploy_service(username, passwd, hosts, extras):

	ruta = os.path.join(ROLESDIR, 'ansible-role-mailserver/site.yml')
	
	pb = PlayBook(playbook=ruta, sudo=True, sudo_pass=passwd, host_list=hosts,
		remote_user=username, extra_vars=extras, callbacks=playbook_cb,
		runner_callbacks=runner_cb, stats=stats)
	
	pb.run()
