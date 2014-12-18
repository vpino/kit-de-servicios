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

import consul
from tastypie import fields
from tastypie.resources import Resource
from tribus.web.api.tasks import queue_service_deploy
from tribus.common.charms.repository import LocalCharmRepository
from tribus.common.charms.directory import CharmDirectory
from tribus.common.recipes.recipe import RecipeDir
from tribus.common.utils import get_path
from tribus.config.base import CHARMSDIR, SERVICEDIR

c = consul.Consul(host='172.17.42.1', port=8500)

class CharmObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}
        
        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data


class ServiceObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}
        
        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data


class ConsulObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}
        
        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data


class ServiceListResource(Resource):
    services = fields.ListField(attribute='services')

    class Meta:
        resource_name = 'services/list'
        object_class = ServiceObject

    def get_object_list(self, bundle):

        SERVICES = LocalCharmRepository(SERVICEDIR)
        
        charms = SERVICES.list()

        l = []

        for ch in charms:
            l.append(ch.metadata.name)

        return [ServiceObject({
                    'services': l
                })]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle)


class ServiceMetadataResource(Resource):
    name = fields.CharField(attribute='name')
    summary = fields.CharField(attribute='summary')
    maintainer = fields.CharField(attribute='maintainer')
    description = fields.CharField(attribute='description')
    components = fields.DictField(attribute='components')

    class Meta:
        resource_name = 'services/metadata'
        object_class = ServiceObject

    def get_object_list(self, bundle):

        if hasattr(bundle.request, 'GET'):
            charm_name = bundle.request.GET.get('name', None)

        SERVICE = RecipeDir(get_path([SERVICEDIR, charm_name]))
        
        return [ServiceObject({
                    'name': SERVICE.metadata.name,
                    'summary': SERVICE.metadata.summary,
                    'maintainer': SERVICE.metadata.maintainer,
                    'description': SERVICE.metadata.description,
                    'components' : SERVICE.metadata.components.items()
                })]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle)


class CharmConfigResource(Resource):
    config = fields.CharField(attribute='config')

    class Meta:
        resource_name = 'charms/config'
        object_class = CharmObject

    def get_object_list(self, bundle):

        if hasattr(bundle.request, 'GET'):
            charm_name = bundle.request.GET.get('name', None)

        CHARM = CharmDirectory(get_path([CHARMSDIR, charm_name]))

        config = {}

        for k, v in CHARM.config._data.iteritems():
            default = v.get('default', None)
            if default:
                config[k] = default

        return [CharmObject({
                    'config': config
                })]

    def obj_get_list(self, bundle, **kwargs):

        return self.get_object_list(bundle)


class ConsulNodesResource(Resource):
    nodes = fields.ListField(attribute='nodes')

    class Meta:
        resource_name = 'consul/nodes'
        object_class = ConsulObject

    def get_object_list(self, bundle):

        NODES = c.catalog.nodes()

        return [ConsulObject({
                    'nodes': NODES
                })]

    def obj_get_list(self, bundle, **kwargs):

        return self.get_object_list(bundle)


class ServiceDeployResource(Resource):
    class Meta:
        resource_name = 'services/deploy'
        object_class = ServiceObject

    def detail_uri_kwargs(self, bundle_or_obj):
        return {}

    def obj_create(self, bundle, **kwargs):
        queue_service_deploy.apply_async([bundle.data])
        return bundle
