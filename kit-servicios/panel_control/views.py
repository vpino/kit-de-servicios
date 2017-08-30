import nmap, shlex, netifaces, os, subprocess, json, paramiko
from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks import add
from common.yml_parse import parseYaml
from config.base import BASE_DIR, SERVICEDIR, RECIPESDIR, SSHDIR, RECI_CONFIG


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
    List all pcs
    """
    default_gateway = netifaces.gateways().get('default').values()[0][0]

    nm = nmap.PortScanner()

    scan_result = nm.scan(default_gateway + "/24", None, '-sP')

    active_hosts = scan_result.get('scan').keys()

    if default_gateway in active_hosts:

        active_hosts.remove(default_gateway)

    return active_hosts

class PcList(APIView):
    """
    List all pcs
    """

    def get(self, request, format=None):
        
        pc = get_active_hosts()

        #lists =dumps(pc)

        return Response(pc)

class ServiceConfigResource(APIView):
    """
    List all parameters to execute the playbook
    """
    def get(self, request, format=None):

        service_name = request.query_params.get('name', None)
        action = request.query_params.get('action', None)

        if service_name is not None:

            try:
                    
                config = {}

                campos = []

                if action == 'install':

                    configdata = json.loads(open(os.path.join(RECIPESDIR, 
                                                            service_name, 
                                                            service_name,
                                                            RECI_CONFIG
                                                            )).read())

                    for r in configdata[action]:

                        campos.append(r)

                    config['message_success'] = configdata['message_success']
                    config['after_installing'] = configdata['after_installing']

                elif action == 'update':

                    configdata = json.loads(open(os.path.join(RECIPESDIR, 
                                                            service_name, 
                                                            service_name,
                                                            RECI_CONFIG
                                                            )).read())

                    campos.append(configdata[action])
                    

                elif action == 'delete':
                    
                    d = {}
                    d['nombre'] = 'delete'
                    campos.append(d)

                
                config['campos'] = campos
                config['receta'] = service_name
                config['ipadd'] = ''
                config['username'] = ''
                config['passwd'] = ''
                config['action'] = ''    
                
                return Response (config)

            except ValueError as e:

                return Response (e, status=status.HTTP_404_NOT_FOUND)
        
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

        print(request.data['config']['campos'])
        
        print 'Task playbook finished? ', result.ready()
        print 'Task result: ', result.get()
             
        return Response(result.get(), status=status.HTTP_201_CREATED)


class ServiceStatus(APIView):
    """
    List Status of the Services
    """

    def get(self, request, format=None):
        
        """
        Variables pasadas por el cliente:
        
            service_name: Nombre del servicio.
            host: Ip donde el servicio va hacer instalado.

        """
        service_name = request.query_params.get('name', None)
        host = request.query_params.get('host', None)
        
        config = {}

        #Lista que contiene toda la info de los servicios de la receta.
        servicios = []

        config['error'] = ''

        #Verificamos que hallan pasado el nombre del servicio y el host
        if service_name and host != '':

            try:

                configdata = json.loads(open(os.path.join(RECIPESDIR, 
                                                            service_name, 
                                                            service_name,
                                                            RECI_CONFIG
                                                            )).read())

                #Procedemos a llenar la data del servicio.
                for servicio in configdata['query']:
                  
                    servicio['status'] = 'Uninstalled'
                    servicio['run'] = 'Inactive'

                    #===== Pasos para comprobar si la receta esta instalada ========
                    
                    #Comando que verifica si el servicio esta instalado
                    command = 'dpkg -l ' + str(servicio['package']) + ' | grep ' + str(servicio['package']) + ' | cut -d " " -f1'
                    
                    #Iniciamos un cliente SSH
                    client = paramiko.SSHClient() 

                    #Agregamos el listado de host conocidos
                    client.load_system_host_keys() 

                    #Si no encuentra el host, lo agrega automaticamente
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

                    #Iniciamos la conexion.
                    client.connect(str(host), username='victor')

                    #Ejecutamos el commando
                    stdin, stdout, stderr = client.exec_command(command)

                    stdout = str(stdout.read())

                    stderr = str(stderr.read())

                    if stdout.strip('\n') == 'ii':

                        servicio['status'] = 'Instalado'

                    if stderr != '':

                        config['error'] = ""

                    #Cerramos la conexion ssh
                    client.close()

                    servicios.append(servicio)

                config['services'] = servicios

            except IOError, e:

                config['error'] = "No pudo conectarse al host digitado."

                return Response(config)

            except Exception, e:

                config['error'] = "No pudo conectarse al host digitado.."

                return Response(config)

        return Response(config)


    def post(self, request, *args, **kwargs):

        config = {}

        servicios = []

        if request.data != '':
            
            try:
                
                for service in request.data['config']['services']:
             
                    #Comprobaremos si el servicio esta corriendo.
                    command = 'sudo -S service ' +  str(service['service']) + ' status | grep active | cut -d " " -f5'

                    #Iniciamos un cliente SSH
                    client = paramiko.SSHClient() 

                    #Agregamos el listado de host conocidos
                    client.load_system_host_keys() 

                    #Si no encuentra el host, lo agrega automaticamente
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 

                    #Iniciamos la conexion.
                    client.connect(str(request.data['config']['ip']), username='kds')

                    #Ejecutamos el commando
                    stdin, stdout, stderr = client.exec_command(command, get_pty = True)
                    
                    if stdout.channel.closed is False: 

                        stdin.write(str(request.data['config']['passwd']) + '\n')
                        stdin.flush()

                    stdout = str(stdout.read())

                    stderr = str(stderr.read())

                    if stdout.strip('\n') == 'active':

                        service['run'] = 'Active'

                    else:

                        service['run'] = 'Inactive'

                        config['error'] = stderr

                    servicios.append(service)

                config['recipe'] = request.data['config']['recipe']
                config['ip'] = request.data['config']['ip']
                config['action'] = request.data['config']['action']
                config['services'] = servicios

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

        with open(SSHDIR, 'r') as key_ssh:
            key['ssh'] = key_ssh.read().replace('\n', '')
       
        return Response(key)

class ServiceRecipeResource(APIView):
    """
    List of All Recipes Available
    """

    def get(self, request, format=None):
        
        recipes = {}

        role = []

        for rol in os.listdir(RECIPESDIR):
            
            r = {}
             
            ROLDIR = os.path.join(RECIPESDIR, rol)

            DATADIR = os.path.join(ROLDIR, rol)

            if os.path.isdir(ROLDIR) and os.path.isdir(DATADIR):

                metadata = json.loads(open(DATADIR+'/metadata.json').read())

                r['name'] = rol
                r['summary'] = metadata[0]['summary']
                r['description'] = metadata[0]['description']

                role.append(r)

        recipes['recipes'] = role

        return Response(recipes)
