import psutil, json, platform, cpuinfo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def sizeof_fmt(num, suffix='B'):
	"""
	Funcion que convierte una cantidad dada a la unidad debida
	"""

	for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
		if abs(num) < 1024.0:
			return "%3.1f%s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f%s%s" % (num, 'Yi', suffix)


def hdInfo():
	"""
    Informacion del hardware que posee la pc
    """
    
	hardware = {}
	hardware['uname'] = {}
	hardware['cpu'] = {}
	hardware['disk'] = {}
	hardware['memory'] = {}

	#Informacion del equipo
	uname = platform.uname()

	hardware['uname']['system'] = uname[0]
	hardware['uname']['name'] = uname[1]
	hardware['uname']['kernel'] = uname[2]
	hardware['uname']['arquitecture'] = uname[4]

	#Informacion del Procesador
	cpu = cpuinfo.get_cpu_info()

	hardware['cpu']['brand'] = cpu.get('brand')
	hardware['cpu']['count'] = cpu.get('count')

	#Informacion del disco duro
	disk = psutil.disk_usage('/')

	hardware['disk']['total'] = sizeof_fmt(disk.total)
	hardware['disk']['free'] = sizeof_fmt(disk.free)
	hardware['disk']['used'] = sizeof_fmt(disk.used)

	#Informacion de la memoria
	memory = psutil.virtual_memory()

	hardware['memory']['total'] = sizeof_fmt(memory.total)
	hardware['memory']['used'] = sizeof_fmt(memory.active)
	hardware['memory']['free'] = sizeof_fmt(memory.inactive)
	
	return hardware

class HardwareInformation(APIView):
	"""
	Information of hardware
	"""

	def get(self, request, format=None):

		hardware = hdInfo()

		return Response(hardware)
