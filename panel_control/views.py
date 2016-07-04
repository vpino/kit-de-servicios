import nmap, shlex, netifaces, json, os
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
from common.ansible_manage import Runner
from tasks import add, tail_logger
from subprocess import check_output
from common.tail_f import TailLog
from common.yml_parse import parseYaml
import os, traceback

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
        
        #tail = TailLog(BASE_DIR+"/", 'playbook-log')

        if recipe_Name != '':

            try:
                
                SERVICE = CharmDirectory(get_path([SERVICEDIR, recipe_Name]))
                                
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
                config['receta'] = recipe_Name
                config['action'] = ''

                return Response (config)

            except:
                
               return Response (status=status.HTTP_404_NOT_FOUND)

        return Response (status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):

        logger_tail = BASE_DIR + '/playbook-log'

        preferences = open(logger_tail, 'w')
        preferences.write(' ')
        preferences.close()

        result = add.delay(
               request.data['config']['ipadd'], 
               request.data['config']['username'], 
               '/recetas/' + request.data['config']['receta'] + '/site.yml', 
               request.data['config']['passwd'], 
               request.data['config']['campos'], 
               4)

        play_log = tail_logger.delay()

        """
        Esta es la manera de ejecutar la receta sin celery:

        runner = Runner(
                request.data['config']['ipadd'], 
                request.data['config']['username'], 
                '/recetas/' + request.data['config']['receta'] + '/site.yml', 
                request.data['config']['passwd'], 
                request.data['config']['campos'], 
                10)

        a = runner.run()

        print 'Task log finished? ', play_log.ready()

        print 'Task playbook finished? ', result.ready()
        print 'Task result: ', result.get()

        """

        preferences = open(logger_tail, 'a') 
        preferences.write('Finnish.\n')
        preferences.close()

        return Response(result.get(), status=status.HTTP_201_CREATED)


class ServiceStatus(APIView):
    """
    List Status of Services
    """

    def get(self, request, format=None):
        
        """
        Variables pasadas por el cliente:
        
            service_name: Nombre del servicio.
            host: Ip donde el servicio va hacer instalado.

        """

        service_name = request.query_params.get('name', None)
        host = request.query_params.get('host', None)
        
        #
        config = {}
        #Diccionario que contiene toda la info de los servicios de la receta.
        servicios = []

        #Verificamos que hallan pasado el nombre del servicio y el host
        if service_name and host != '':

            try:

                #Guardamos en una variable la data del servicio contenida en un yaml
                SERVICE = parseYaml(SERVICEDIR + '/' + service_name , '/config.yaml' )
                
                #Procedemos a llenar la data del servicio.
                for k, v in SERVICE['consult'].iteritems():
                    d = {}
                    d['service'] = k
                    d['nombre'] = v.get('name', None)
                    d['description'] = v.get('description', None)
                    d['status'] = 'Desintalado'
                    d['run'] = 'Offline'

                    #Comprobaremos si el servicio esta instalado.
                    consult = 'ssh kds@' + str(host) + ' dpkg -l ' + str(d['service']) + ' grep  ii | cut -d "v" -f1'

                    #Tipo de error:CalledProcessError

                    command_install = shlex.split(consult)
                    
                    command_install = check_output(command_install)

                    command_install = command_line.strip('\n')

                    if command_line:

                        d['status'] = 'Instalado'

                    #Comprobaremos si el servicio esta corriendo.

                    consult = 'ssh kds@' + str(host) + ' /etc/init.d/' +  str(d['service']) + ' status | grep active | cut -d " " -f5'

                    command_running = shlex.split(consult)
                    
                    command_running = check_output(command_running)

                    command_running = command_line.strip('\n')

                    if command_running:

                        d['run'] = 'Online'


                    servicios.append(d)

            except Exception,e: 
                config['error'] = str(e)

                print str(e)

                return Response(config)

        return Response(config)