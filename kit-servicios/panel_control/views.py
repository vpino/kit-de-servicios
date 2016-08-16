import nmap, shlex, netifaces, json, os, subprocess
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
from common.tail_f import TailLog
from common.yml_parse import parseYaml

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

    def get(self, request, format=None):
        
        pc = get_active_hosts()

        #lists = json.dumps(pc)

        return Response(pc)

class ServiceMetadataResource(APIView):
    """
    List all Recipes
    """

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
    
    def get(self, request, format=None):

        service_name = request.query_params.get('name', None)
        action = request.query_params.get('action', None)

        #tail = TailLog(BASE_DIR+"/", 'playbook-log')

        if service_name != '':

            try:
                    
                config = {}

                campos = []

                if action == 'install':

                    SERVICE = CharmDirectory(get_path([SERVICEDIR, service_name]))

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
                    config['receta'] = service_name
                    config['action'] = ''

                if action == 'update':

                    SERVICE = parseYaml(SERVICEDIR + '/' + service_name , '/config.yaml' )

                    for k, v in SERVICE['update'].iteritems():

                        d = {}

                        d['field_name'] = k
                        d['nombre'] = v.get('name', None)
                        d['default'] = v.get('default', None)
                        d['tipo'] = v.get('type', None)
                        d['items'] = v.get('items', None)
                        campos.append(d)

                    config['campos'] = campos
                    config['username'] = ''
                    config['passwd'] = ''
                    config['receta'] = service_name
                    config['action'] = ''

                if action == 'delete':

                    SERVICE = parseYaml(SERVICEDIR + '/' + service_name , '/config.yaml' )
                    
                    d = {}
                    d['nombre'] = 'delete'
                    campos.append(d)

                    config['campos'] = campos
                    config['username'] = ''
                    config['passwd'] = ''
                    config['receta'] = service_name
                    config['action'] = ''

                return Response (config)

            except:
                
               return Response (status=status.HTTP_404_NOT_FOUND)

        return Response (status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):

        result = add.delay(
               request.data['config']['ipadd'], 
               request.data['config']['username'], 
               '/recetas/' + request.data['config']['receta'] + '/site.yml', 
               request.data['config']['passwd'], 
               request.data['config']['campos'], 
               4)

        print 'Task playbook finished? ', result.ready()
        print 'Task result: ', result.get()
             
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

        config['error'] = ''

        #Verificamos que hallan pasado el nombre del servicio y el host
        if service_name and host != '':

            try:
                #Guardamos en una variable la data del servicio contenida en un yaml
                SERVICE = parseYaml(SERVICEDIR + '/' + service_name , '/config.yaml')
                
                #Procedemos a llenar la data del servicio.
                for k, v in SERVICE['query'].iteritems():
                    d = {}
                    d['service'] = k
                    d['package'] = v.get('package', None)
                    d['description'] = v.get('description', None)
                    d['status'] = 'Desintalado'
                    d['run'] = 'Offline'

                    #Comprobaremos si el servicio esta instalado.
                    query = 'ssh kds@' + str(host) + ' dpkg -l ' + str(d['package']) + ' | grep ' + str(d['package']) + ' | cut -d " " -f1'
                  
                    command_install = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    
                    check_success, check_err = command_install.communicate()

                    if check_success.strip('\n') == 'ii':

                        d['status'] = 'Instalado'

                    if check_err != '':

                        if check_err.split(':')[0] == 'ssh':

                            config['error'] = "La ip digitada es incorrecta y/o presenta problemas."

                    servicios.append(d)

                config['services'] = servicios

            except IOError, e:

                config['error'] = "El Servicio que intenta instalar no esta disponible."

                return Response(config)

        return Response(config)


    def post(self, request, *args, **kwargs):

        config = {}
        servicios = []

        config['error'] = ''

        if request.data != '':
            
            try:
                
                for service in request.data['data']['services']:

                    d = {}
                    d['service'] = service['service']
                    d['run'] = service['run']

                    #Comprobaremos si el servicio esta corriendo.
                    query = 'ssh kds@' + str(request.data['data']['ip']) + ' echo ' + str(request.data['data']['passwd']) + ' | sudo -S service ' +  str(service['service']) + ' status | grep active | cut -d " " -f5'

                    command_running = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                    running_success, running_err = command_running.communicate()
                
                    if running_success.strip('\n') == 'active':

                        service['run'] = 'Online'

                    else:

                        service['run'] = 'Offline'

                        config['error'] = config['error'] + running_err

                    servicios.append(d)

                config['services'] = servicios
                config['ip'] = request.data['data']['ip']
                config['recipe'] = request.data['data']['recipe']

            except IOError, e:

                config['error'] = e

                return Response(config)
            
            except KeyError:

                config['error'] = 'La informacion pasada es invalida y/o incorrecta'

                return Response(config)

            except Exception, e:
        
                config['error'] = e

                return Response(config)


        return Response(config)

class ServiceKeyResource(APIView):
    """
    List Key ssh
    """

    def get(self, request, format=None):
        
        key = {}

        with open('/home/kds/.ssh/id_rsa.pub', 'r') as key_ssh:
            key['ssh'] = key_ssh.read().replace('\n', '')
       
        return Response(key)

        