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

# """

# This script invokes the setuptools script for Tribus.

# For more information about this file, see documentation on
# ``tribus/common/setup/utils.py``

# """

# from setuptools import setup

# from tribus import BASEDIR
# from tribus.common.setup.utils import get_setup_data

# setup(**get_setup_data(BASEDIR))

#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name="kds",
    packages=find_packages(),
    version="1.0",
    install_requires=[
        "django >= 1.7",
    ],
    package_data = {
        '': [".txt", ".png", ".html", ".css", ".jpeg", ".js"]
    },
    zip_safe=False,
    include_package_data=True
)
