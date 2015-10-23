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


"""

This package contains remote execution scripts based on Fabric.

This package is intended to serve as an automation library. It is designed to
execute (local) operations on KDS's development environment (Docker,
Vagrant, chroot, etc), and also on (remote) servers when deploying Charms.

"""

import os
import pwd
from fabric.api import env, local
from kds import BASEDIR
from kds.config.base import CONFDIR, AUTHOR, AUTHOR_EMAIL
from kds.config.ldap import (AUTH_LDAP_SERVER_URI,
                                AUTH_LDAP_BIND_DN, AUTH_LDAP_BIND_PASSWORD)
#from kds.config.pkg import (python_dependencies, debian_run_dependencies,
                               #debian_build_dependencies)
from kds.common.utils import get_path
from kds.common.system import get_local_arch
#from kds.common.fabric.docker import *
#from kds.common.fabric.django import *
#from kds.common.fabric.setup import *


# Fabric environment configuration
env.basedir = BASEDIR
env.host_string = '127.0.0.1'
env.user = str(pwd.getpwuid(os.getuid()).pw_name)
env.user_id = str(pwd.getpwuid(os.getuid()).pw_uid)
env.port = 22222
env.password = 'tribus'
env.warn_only = True
env.output_prefix = False
env.arch = get_local_arch()
