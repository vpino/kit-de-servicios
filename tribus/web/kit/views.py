#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tribus.config.brand import TRIBUS_SPONSORS
from django.shortcuts import render
# from tribus.web.registration.forms import SignupForm
from haystack.query import SearchQuerySet
from django.core.paginator import Paginator, InvalidPage
from django.contrib.contenttypes.models import ContentType


def kit(request):

    # Cargamos la librería AngujarJS junto con sus plugins
    # render_js = ['angular', 'angular.sanitize', 'angular.resource',
    #                 'angular.bootstrap']

    # Cargamos las funciones de Tribus para AngularJS
    # render_js += ['controllers.angular', 'services.angular',
    #                 'elements.angular', 'search.angular',
    #                 'navbar.angular']

    # context["render_js"] = render_js
    context = {}

    return render(request, 'kit/base-kit.html', context)
