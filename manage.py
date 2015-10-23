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

This file is an entry point for managing KDS in development mode.

"""

#import sys
#from django.core.management import execute_from_command_line

#execute_from_command_line(sys.argv)

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kds.config.web")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
