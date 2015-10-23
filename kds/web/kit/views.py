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

from django.shortcuts import render


def kit(request):
    context = {}
    #Cargamos la librería AngujarJS junto con sus plugins
    render_js = ['jQuery', 'angular', 'hamster', 'angular.resource', 'angular.bootstrap', 
                 'bootstrap','angular.draganddrop', 'angular.mousewheel'
                ]

    #Cargamos las funciones de Tribus para AngularJS
    render_js += ['controllers.angular', 'services.angular', 'kit.angular','panzoom.angular',
                  'panzoomwidget.angular'
                 ]

    context["render_js"] = render_js

    return render(request, 'kit/base-kit.html', context)
