#!/bin/bash
# Proposito: con este script deseamos proveer una herramienta para probar
#            el funcionamiento de la receta de Kit de Servicios de DNS.
# Autor: Joaquin Muñoz Lucavechi

echo "El objetivo de este script es asistir en la configuración del nombre\n \
de dominio institucional y el servicio de resolución de ese nombre de dominio\n \
a escala global.\n \
Para ello, primero estableceremos el nombre de dominio institucional y así\n \
comenzar a definir el archivo de zona DNS. Seguidamente pasaremos a configurar\n \
el (primer) servidor de nombre de la zona DNS con lo cual se hace operativa\n \
la resolución de nombres."

echo "Introduzca el nombre de dominio de su institucion [por ejemplo: institucion.gob.ve]:"
read dominio

echo "Vamos a configurar el primer servidor de nombre de la zona ${dominio}."

echo "Introduzca el nombre de servidor de DNS que desea configurar inicialmente\n \
[por ejemplo: ns]:"
read nombre

echo "Introduzca el número de IPv4 del servidor de nombre \'${nombre} [por ejemplo: 192.168.1.53]:"\n \
read ipv4

echo
