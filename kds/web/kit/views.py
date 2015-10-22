#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
