==========================
Problemas Kit de servicios

***************************
ENTORNO DE KIT DE SERVICIOS

- Cuando se intenta desplegar un servicio mediante el comando 'local()' de Fabric lo estamos ejecutando DENTRO del contenedor, es posible que encontremos el directorio de Kit de servicios, pero estamos en el sistema de archivos del contenedor y cualquier cambio que se haga solo tendra efecto en el contenedor. Por otra parte dentro del contenedor no esta presente 'docker' razon por la que aun pudiendo asignar correctamente los permisos aun no seria posible crear los contenedores. Si se provee la direccion IP de la interfaz a traves de la cual esta conectada el dispositivo de red activo, entonces se puede acceder a la maquina local y de esa forma si se pueden ejecutar los comandos de docker.

- Mantener las imagenes y contenedores generadas mediante dockerfiles se esta haciendo muy complicado. Las imagenes creadas solo son utiles durante el tiempo que los contenedores esten funcionando. Cuando un contenedor se detiene y se vuelve a iniciar, cambia su direccion IP interna y toda la configuración hecha necesita ser actualizada.

- Seria util definir cuales son los elementos de Tribus que se estan utilizando en Kit de servicios. ¿Podria Kit de servicios sostenerse como una aplicación Web independiente, sin necesidad de funcionar en un entorno virtualizado?

--------
CREACION

- Hacer un usuario para Canaima que suba sus imagenes al indice de docker.

----------
DESARROLLO

----------
PRODUCCION


***************************
VIRTUALIZACION DE SERVICIOS

- Tarea: Hacer lo que hago con un dockerfile sencillo (el de consul por ejemplo) con bash


******
CONSUL

- Aclarar cual es el problema con el esquema actual que necesita un directorio para i386 y uno para amd64
- Mecanismo para consultar estado de los servicios a traves de Consul o alguna solución similar. Utilizando consul es posible monitorear los servicios creados y consultar su estado de una forma relativamente sencilla. El unico inconveniente es que seria necesario crear una API que consulte la API de consul para que se la sirva a la interfaz de Kit de servicios.
- Como se utilizara consul. Es necesario virtualizarlo?
- Hacer correr consul en el bridge de docker
- Hacer correr consul en local
- Hacer uso del .deb qu esta hosteado en alguna parte para facilitar la instalacion del paquete correspondiente de consul


*********
SERVICIOS

------------------------
MODULO QUE LEE SERVICIOS

- Mejorar modulo interno encargado de leer Servicios y Componentes.

********************
COMPONENTES (CHARMS)

--------------------------
MODULO QUE LEE COMPONENTES

- Mejorar modulo interno encargado de leer Servicios y Componentes.

------------------
INTERFAZ & BACKEND

- Se necesita una forma de que las peticiones enviadas al servidor muestren su progreso. Debe existir algo entre la interfaz y la API del servidor que permita consultar el estado de una tarea o proceso. Puede ser con Celery que tiene una forma de consultar las tareas e indicar si se completaron o no.

- Por si no lo coloque, las tareas de celery necesitan ser monitoreadas desde la interfaz.

- Falta la autenticacion y login al sistema de Kit de servicios

- Los recursos de la API deben tener sus autorizaciones correspondientes segun el objetivo de cada recurso y el nivel de seguridad adecuado en caso de manejar datos sensibles.

- Todo el codigo necesita pruebas.

- Limpiar Navbar.

- Separar sidebar del Panzoom.

