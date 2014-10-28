.. _planificacion:

==============================
Planificación Kit de servicios
==============================

Automatización de servicios
===========================

Servicios por automatizar
*************************

- DHCP
- DNS
- LDAP
- CORREO
- WIKI*

Investigaciones pendientes
**************************

- Entender el funcionamiento básico de Xen, para crear y gestionar maquinas virtuales. Manejar contenedores Xen (crearlos, verificar existencia, conectarse a ellos, modificarlos, eliminarlos, etc)
- Como generar/obtener la imagen base para crear los servicios virtualizados (Xen)
- Mejorar configuración de consul para utilizarlo como orquestador de despliegue
- Pruebas de seguridad: como evitar exponer informacion sensible al exterior pero permitiendo a los servicios internos acceder a la misma
- Como utilizar Consul en contenedores Xen
- Crear checks dinamicamente
- Como recibir los parametros de configuración de los servicios desde la interfaz
- Como proveer feedback a la interfaz del estado de los procesos y otras acciones
- Empaquetamiento de Consul

Estimación de tiempo
********************

- La investigación para conocer el servicio de Wiki tardo 1 mes
- Automatizar la instalación del servicio de wiki se llevo 2 semanas
- Se estima que para automatizar un servicio se necesitan 6 semanas por servicio
- Automatizar 4 servicios se tomaria entonces 24 semanas/6 meses ocupando una sola persona 8 horas diarias
- La investigación y pruebas para crear recetas de servicios en Xen puede llevar 2 semanas
- Se estima que la creación de una interfaz de linea de comandos para el despliegue basico de servicios se lleve 2 semanas

Configuración a traves de la API
==================================

Conexión con la interfaz
========================

Componentes de la interfaz
**************************

- Pantalla de Login
- Pantalla principal
- Dialogo de descripción del servicio
- Dialogo de descripción del equipo
- Dialogo de configuración y despliegue de servicio

Acciones de la interfaz
***********************

- Mostrar equipos (fisicos) disponibles
- Mostrar servicios disponibles para despliegue
- Mostrar estado de un equipo
- Mostrar estado de un servicio
- Mostrar servicios detectados en un equipo 
- Configurar y desplegar servicio
- Configurar equipo para despliegue de servicios
- Mostrar progreso/estado de una peticion/accion
- Actualizar configuración de un servicio existente

Investigaciones pendientes
**************************

- Como llenar un modal
- Cambio entre pestañas del modal
- Consultas a la API desde la interfaz
- Dibujar representación de los servidores
- Agregar y borrar elementos dinamicamente del Panzoom
- Scroll para la lista de servicio disponibles
- Integrar barras de estado de bootstrap
- Feedback de las acciones ejecutadas (obtener respuesta del estado de las peticiones hechas al backend)

Tareas
******

- Actualizar librerias
- Limpiar proyecto 
-- Determinar elementos reusables
-- Reconfigurar URLs, Vistas, etc
-- Borrar plantillas y librerias no utilizadas
- Definir estilo visual/grafico de la interfaz
-- Arte grafico que sera utilizado
-- Plantilla base
- Creación de modelos para el Login
- Creación de la vista para la pantalla principal
- Creación de la vista para el Login 
-- Autenticación
-- Redirección
-- Validación
- Creación de la plantilla para la pantalla principal
- Creación de la plantilla para el login
- Validación del Login en el cliente* 

Estimación de tiempo
********************

- Actualización de librerias; determinar las versiones que mejor se ajustan a los requerimientos del kit de servicios: Entre 2 y 5 dias
- Crear plantillas base con los estilos minimos necesarios: 3 horas de trabajo en 1 dia
- Determinar elementos de la interfaz de tribus que seran reutilizados en el kit de servicios: Entre 1 y 2 dias
- Diseñar interfaz (plantillas, html, css): Entre 2 y 4 dias
- Pruebas y corrección de errores: Continuamente, 1 dia por cada actividad mencionada anteriormente
