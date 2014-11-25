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

from django.views.generic.base import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tribus.web.api import api_01

admin.autodiscover()

urlpatterns = patterns(
    '',
    #url(regex=r'^$', view='tribus.web.views.index'),
    url(regex=r'^prueba/$', view='tribus.web.views.prueba'),
    url(regex=r'^kit/$', view='tribus.web.kit.views.kit'),
    url(regex=r'^api/', view=include(api_01.urls)),
)
