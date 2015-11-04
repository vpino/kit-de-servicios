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

from tastypie import fields
from tastypie.resources import Resource
from kds.web.api.tasks import queue_service_deploy, saludar
from kds.common.charms.repository import LocalCharmRepository
from kds.common.charms.directory import CharmDirectory
from kds.common.recipes.recipe import RecipeDir
from kds.common.utils import get_path
from kds.config.base import SERVICEDIR


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
        resource_name = 'service/metadata'
        object_class = ServiceObject

    def get_object_list(self, bundle):

        if hasattr(bundle.request, 'GET'):
            service_name = bundle.request.GET.get('name', None)

        SERVICE = RecipeDir(get_path([SERVICEDIR, service_name]))
        
        return [ServiceObject({
                    'name': SERVICE.metadata.name,
                    'summary': SERVICE.metadata.summary,
                    'maintainer': SERVICE.metadata.maintainer,
                    'description': SERVICE.metadata.description,
                    'components' : SERVICE.metadata.components.items()
                })]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle)


class ServiceConfigResource(Resource):
    
    config = fields.DictField(attribute='config')

    class Meta:
        resource_name = 'service/config'
        object_class = ServiceObject

    def get_object_list(self, bundle):

        if hasattr(bundle.request, 'GET'):
            service_name = bundle.request.GET.get('name', None)
        
        SERVICE = CharmDirectory(get_path([SERVICEDIR, service_name]))
        
        config = {}

        campos = []

        for k, v in SERVICE.config._data.iteritems():
            d = {}
            d['field_name'] = k
            d['nombre'] = v.get('name', None)
            d['default'] = v.get('default', None)
            d['tipo'] = v.get('type', None)
            campos.append(d)

        config['campos'] = campos
        config['ipadd'] = ''
        config['username'] = ''
        config['passwd'] = ''

        return [ServiceObject({'config': config})]

    def obj_get_list(self, bundle, **kwargs):

        return self.get_object_list(bundle)


class ServiceDeployResource(Resource):
    class Meta:
        resource_name = 'service/deploy'
        object_class = ServiceObject

    def detail_uri_kwargs(self, bundle_or_obj):
        return {}

    def obj_create(self, bundle, **kwargs):
        #saludar.apply_async([bundle.data])
        queue_service_deploy.apply_async([bundle.data])
        return bundle
