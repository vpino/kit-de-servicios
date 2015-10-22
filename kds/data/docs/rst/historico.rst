****************************************
Funcionalidades en Canaima Instituciones


- Activar y desactivar modulos a traves del panel de administracion (Feature flipping)
- Asistente de configuracion de servicios
- Interfaz para activar y desactivar modulos
- Crear y manejar grupos de usuarios conjuntamente con el LDAP para determinar los permisos para cada tipo de usuario.
- Mapear permisos de usuarios desde el LDAP
- Asistente de configuración "Primera Vez"
- Gestionar los roles en LDAP a traves de grupos


Durante la creación del entorno de desarrollo se deben crear los flags o switches correspondientes a cada modulo

Los switches se deben colocar en:

- Vistas
- Modulos de angular
- Plantillas HTML
- Recursos de la API y en controladores de Angular

Hay modulos transversales a toda la plataforma (como el buscador), que debe tener acceso (dinamico, sujeto a disponibilidad y permisos) a datos de otros modulos


******************************
Funcionalidad Kit de servicios

- Listar servicios disponibles para desplegar en maquinas remotas

- Listar maquinas remotas accesibles, en donde se pueden desplegar servicios

- Ver información basica y avanzada de un servicio

- Ver información bascia y avanzada de una maquina fisica y de los servicios presentes en ella

- Ejecutar acciones en las maquinas remotas (listar, instalar, configurar, eliminar; servicios)

*****
F.A.Q


1. ¿Porque usar solo Angular.JS?

R: Mantener el minimo posible de componentes para facilitar el mantenimiento y la integración de nuevos participantes al proyecto. Mejora el rendimiento en la carga de la pagina.

2. ¿Porque usar Docker para gestionar el entorno?

R: Aislamiento, automatización y automantenimiento del espacio de trabajo


3. ¿Que hace Zookeeper?

R: Almacena la configuracion de las relaciones entre servicios, sincroniza la ejecucion de tareas entre servicios, vigila el estado de los servicios, los cambios en su configuracion y relaciones. Es un gestor de configuracion distribuida (Cluster Coordination Service)
