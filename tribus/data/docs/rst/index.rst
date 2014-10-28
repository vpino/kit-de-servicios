======
Canaima Instituciones
======

.. include:: readme.rst

Para ello se plantea el siguiente plan de trabajo:

* Diseño y planificación preliminar.
* Documentación de procesos iniciales.
* Captación de colaboradores.
* Organización del trabajo colaborativo.
* Ejecución de la planificación.
* Entrega del producto.

Diseño y Planificación Preliminar
===============

Paradigmas de trabajo
---------------

Se plantea un proceso de desarrollo colaborativo, basado en los preceptos del Software Libre y la metodología de desarrollo de sistemas basados en Canaima GNU/Linux. Para ello se sugerirán herramientas para la gestión de proyectos, versionamiento de código, generación de documentación, empaquetamiento, compilación de paquetes e integración continua.

Necesidades
---------------

Con base en las inquietudes formuladas por los usuarios en los mecanismos de Soporte Técnico de la distribución Canaima Popular, información recopilada desde la base de datos de la Oficina de Consultoría al Estado, entre otros instrumentos de recolección de datos, se han recopilado las siguientes necesidades, las cuales deben servir como insumo para la generación de los objetivos que deben guiar el desarrollo de Canaima Instituciones:

* Asistente para instalación remota de imágenes para escritorio del Sistema Operativo Canaima Instituciones desde una estación central de trabajo.
* Gestor de configuraciones que permita agrupar las aplicaciones y comportamiento deseado por Oficina/Gerencia, permitiendo agilizar la puesta en marcha de estaciones de trabajo desde una estación central de trabajo.
* Asistente para la instalación y configuración de servicios comunes en servidores de aplicaciones.
* Configuración de las estaciones de trabajo que requieran conectar aplicaciones cliente a los servicios de la institución.

Propuestas
---------------

Para atender las necesidades planteadas, se realizan las siguientes propuestas:

* Asistente para instalación remota de imágenes para escritorio del Sistema Operativo Canaima Instituciones desde una estación central de trabajo.


    * Realización de una imagen de Sistema Operativo base que contenga los elementos básicos para el arranque del sistema. Se propone una metodología de trabajo similar a la utilizada en Canaima Popular con Canaima Semilla.

    * Generación de una interfaz web accesible a través de una dirección IP interna, que permita ejecutar los pasos de instalación desde una estación central de trabajo. La interfaz debe poder permitir seleccionar de una lista los equipos encendidos que se encuentran en las redes internas de la institución. Se propone reutilizar la aplicación en desarrollo “Tribus”, que implementa el gestor de instalaciones remotas `FAI <http://fai-project.org/>`_.

* Gestor de configuraciones que permita agrupar las aplicaciones y comportamiento deseado por Oficina/Gerencia, permitiendo agilizar la puesta en marcha de estaciones de trabajo desde una estación central de trabajo.

    * Generación de una interfaz web que permita manejar remotamente las configuraciones y paquetes de las estaciones de trabajo, basándose en perfiles según Oficina/Gerencia. Se propone reutilizar la aplicación en desarrollo “Tribus”, que implementa el gestor de operaciones remotas `Fabric <http://docs.fabfile.org/en/1.7/>`_.

* Asistente para la instalación y configuración de servicios comunes en servidores de aplicaciones.
* Configuración de las estaciones de trabajo que requieran conectar aplicaciones cliente a los servicios de la institución.
* Generación de una interfaz web que permita listar, remover y/o añadir servicios en un servidor de trabajo. También debe permitir instalar los clientes de aplicación que se conectan a los servidores de trabajo, según Oficina/Gerencia.

.. _ideas:

Ideas para la presentación 
---------------

Se recuerda, por principios de 2009, a un CNTI destinando todos sus recursos institucionales a la tarea de migración a Software Libre en la APN que le había sido encomendado, primero por el ministerio  Ciencia por el . Por falta de información, no se puede asegurar bien cómo se construye esa estrategia, pero si se interpretan los indicadores tomados en cuenta desde ese entonces, se puede decir que la migración tenía tres aspectos fundamentales:

#. La parte de servicios, servidores y todo lo que tiene que ver con plataforma e infraestructura.
#. La parte de clientes, es decir, estaciones de trabajo, en base a la cual se desarrolla tácitamente la distribución nacional de Software Libre.
#. La parte que tiene que ver con la formación de los trabajadores de la APN.

`Aquí <http://www.softwarelibre.gob.ve/index.php?option=com_content&view=article&id=104&Itemid=80>`_ se puede revisar la información a la cual se hace referencia: 

En cuanto a (1), una táctica fue desarrollar una guía documentada de implementación de servicios. A ese proyecto se le denominó Kit de servicios, el cual puede revisarse `aquí <http://wiki.canaima.softwarelibre.gob.ve/wiki/Kit_de_Servicios>`_

Kit de Servicios fue un proyecto llevado a cabo por diversos talentos de la Gerencia de Plataforma Tecnológica, pero con el trabajo de investigación base de Jesús Lara, quien para ese entonces trabajaba en la Cooperativa Venezolana de Tecnologías Libres (COVETEL).

Un primer ensayo del Kit de Servicios se desplegó en los servidores del CNTI. Esta dinámica de ensayos se gestó de la misma manera cuando se desarrolló la primera versión de la distribución de Software Libre para el Estado.

Una segunda versión de Kit de Servicios era pensada para llevarla a la reciente distribución estable de aquel entonces: squeeze. Este trabajo nunca se desarrolló.

.. _installation:

Instalación
===========

TODO

.. toctree::
    :maxdepth: 1

    installation
    services
    technology

Configuración
-------------

TODO

.. toctree::
    :maxdepth: 1
    :glob:

    configuration/*


Documentación para desarrolladores
==================================

TODO

.. toctree::
    :maxdepth: 1

.. _api_docs:

Documentación de la API
-----------------------

TODO

.. toctree::
    :maxdepth: 1
    :glob:

    
.. _roadmap:

Hojas de ruta
-------------

TODO

.. _changelog:

Lista de cambios
----------------

TODO

.. _license:

Licencia de distribución
------------------------

Canaima Instituciones está licenciado bajo **GPL-3**. Todas las contribuciones hechas por otros desarrolladores serán redistribuídas dentro de Tribus bajo la misma licencia, a menos que se especifique lo contrario. Es necesario hacer notar que las porciones de código que estén licenciadas bajo términos incompatibles con los de la licencia GPL-3 y deseen ser incorporados a Tribus, serán objeto de rechazo.

.. toctree::
    :maxdepth: 1

    copying
    contributors
    license

.. _help:

Obtener ayuda
=============

Si ya has leído el :ref:`tutorial`, la :ref:`usage_docs`, las :ref:`faq` y la :ref:`api_docs`, y no has podido encontrar la solución a tus problemas, puedes consultar a alguno de los recursos que se listan más abajo. Sin embargo, asegúrate de leer bien todos los recursos de documentación que están disponibles **antes** de hacer un ticket de error o enviar un correo a la lista.

.. _mail_list:

Foro
----

TODO

Bugs/ticket tracker
-------------------

Puedes revisar si ya se ha reportado un error relacionado con el problema que estás presentando en el gestor de `tickets <https://github.com/tribusdev/canaima-instituciones/issues>`_.

Twitter
-------

TODO

Grupo en Facebook
-----------------

TODO

IRC
---

TODO

Colaboradores
---------------

* Luis Martínez como principal redactor del documento en su primera versión.
* Joaquin Muñoz Lucavechi, en la sección :ref:`Ideas para la presentación <ideas>`.
