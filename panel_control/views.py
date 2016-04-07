from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import Http404
from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from common.charms.repository import LocalCharmRepository
from common.charms.directory import CharmDirectory
from common.recipes.recipe import RecipeDir
from common.utils import get_path
import nmap 
import netifaces
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICEDIR = BASE_DIR + '/data/services'

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


def homepage(request):

    return render_to_response('index.html',
                              context_instance=RequestContext(request))



def get_active_hosts():
    """
    List all pcs, conectados al servidor
    """
    """
    default_gateway = netifaces.gateways().get('default').values()[0][0]

    nm = nmap.PortScanner()

    scan_result = nm.scan(default_gateway + "/24", None, '-sP')

    active_hosts = scan_result.get('scan').keys()

    if default_gateway in active_hosts:

        active_hosts.remove(default_gateway)

    return active_hosts
    """

    return {"10.16.106.147"}

class PcList(APIView):
    """
    List all pcs, conectados al servidor
    """

    #Especificamos como retornara la data, en este caso formato json
    #renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        
        pc = get_active_hosts()

        #lists = json.dumps(pc)

        return Response(pc)

class ServiceMetadataResource(APIView):
    """
    List all Recipes
    """

    #Especificamos como retornara la data, en este caso formato json
    #renderer_classes = (JSONRenderer, )

    def get(self, request, service_name, format=None):
        
        SERVICE = RecipeDir(get_path([SERVICEDIR, 'service_name']))
        
        return Response([ServiceObject({
                    'name': SERVICE.metadata.name,
                    'summary': SERVICE.metadata.summary,
                    'maintainer': SERVICE.metadata.maintainer,
                    'description': SERVICE.metadata.description,
                    'components' : SERVICE.metadata.components.items()
                })])

class ServiceConfigResource(APIView):
    """
    List all parametros para ejecutar el playbook
    """

    #Especificamos como retornara la data, en este caso formato json
    #renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):

        recipe_Name = request.query_params.get('name', None)
        
        if recipe_Name:

            SERVICE = CharmDirectory(get_path([SERVICEDIR, recipe_Name]))
            
            if SERVICE:
            
                config = {}

                campos = []

                for k, v in SERVICE.config._data.iteritems():
                    d = {}
                    d['field_name'] = k
                    d['nombre'] = v.get('name', None)
                    d['default'] = v.get('default', None)
                    d['tipo'] = v.get('type', None)
                    d['items'] = v.get('items', None)
                    campos.append(d)

                config['campos'] = campos
                config['ipadd'] = ''
                config['username'] = ''
                config['passwd'] = ''

                return Response (config)

            else:

                return Response (status=status.HTTP_404_NOT_FOUND)

        return Response (status=status.HTTP_404_NOT_FOUND)






    def post(self, request, *args, **kwargs):

        print request
        print args
