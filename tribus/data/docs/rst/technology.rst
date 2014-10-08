.. _docker:

===========
Tecnologias
===========

.. _docker:


Docker
======

Docker es una capa de abstraccion sobre `Linux Containers <https://linuxcontainers.org/>`_, que es facil de usar para los desarrolladores. Docker facilita el uso de contenedores sin necesidad de adentrarse en los detalles ni conocer en profundidad esta tecnología, por lo cual es considerada como la mejor aproximación para manejar contenedores en linux. 

.. _containers:

Linux Containers
****************

Los contenedores pueden definirse como maquinas virtuales ligeras que cuentan con su propia interfaz de red, espacio para ejecutar procesos aislados del huesped, no necesitan emular dispositivos. A pesar de que los procesos se ejecutan de forma aislada estos se ejecutan directamente en el host. El rendimiento en terminos de CPU, memoria y red es casi nativo. Los contenedores inician casi al instante.

La filosofia de docker exige que los archivos de configuración, dependencias y todo lo que se necesita para que una aplicació/servicio funcione, se encuentre dentro del contenedor. El mecanismo de conexión con el exterior son los puertos y la interfaz que provee el mismo docker.

Un beneficio de este planteamiento es que las aplicaciones tienen un alto nivel de portabilidad. Se presume que la propuesta de servicios orientada hacia la portabilidad terminara imponiendose tarde o temprano.

El problema que pretende solucionar docker es el despliegue de servicios y aplicaciones en multiples y distintas plataformas de software y hardware, que sirven para distintos propositos. La solucion propuesta consiste en proveer un mecanismo de encapsulamiento ubicuo, para los distintos tipos de servicios/aplicaciones que se desean desplegar y que sea docker el encargado de los detalles de implementación en las distintas plataformas objetivo.

.. _ventajas:

Ventajas de Docker
******************

* Aplicaciones autocontenidas, es decir: la aplicación tiene todo lo que necesita en un sistema de archivos exclusivo para ella. Falta definir porque esto es algo bueno.

* En docker las aplicaciones comparten un mismo kernel. Esto parece ser util para el despliegue de aplicaciones en la nube.

Las ventajas que ofrecen los contenedores por si solas no resuelven ningun problema con respecto a otras tecnologiasde virtualización. Basicamente ofrecen mejoras en terminos de rendimiento y portabilidad.

.. _herramientas:

Herramientas potencialmente utiles para Canaima Instituciones
*************************************************************

* `Embassy <https://github.com/progrium/embassy>`_
* `Ambassadord <https://github.com/progrium/ambassadord>`_
* `Registrator <https://github.com/progrium/registrator>`_
* `MaestroNG <https://github.com/signalfuse/maestro-ng>`_
* `Shipper <https://github.com/mailgun/shipper>`_

.. _enlaces:

Enlaces y documentación
***********************

* `Introduccion a docker <http://www.centurylinklabs.com/what-is-docker-and-when-to-use-it/>`_

* `Sistemas de archivos soportados por docker <http://www.projectatomic.io/docs/filesystems/>`_

* `Manejo de data con contenedores 1 <http://www.projectatomic.io/docs/filesystems/>`_

* `Manejo de data con contenedores 2 <http://docs.docker.com/userguide/dockervolumes/>`_

* `Manejo de data con contenedores 3 <http://www.offermann.us/2013/12/tiny-docker-pieces-loosely-joined.html>`_ (Puede que este un poco obsoleto por usar docker 0.7)

* `Manejo de data con contenedores 4 <http://stackoverflow.com/questions/18496940/how-to-deal-with-persistent-storage-e-g-databases-in-docker>`_

* `Automatizacion con dockerfiles <https://www.digitalocean.com/community/tutorials/docker-explained-using-dockerfiles-to-automate-building-of-images>`_

* `Multiserver dockers with ambassadors <http://www.centurylinklabs.com/deploying-multi-server-docker-apps-with-ambassadors/?hvid=XxIzL>`_

* `Creando un contenedor de mysql <http://txt.fliglio.com/2013/11/creating-a-mysql-docker-container/>`_

* `Diferencias entre docker y una maquina virtual <http://stackoverflow.com/questions/16047306/how-is-docker-io-different-from-a-normal-virtual-machine>`_

* `Kernel namespaces <http://blog.dotcloud.com/under-the-hood-linux-kernels-on-dotcloud-part>`_

* `Un vistazo a docker <http://www.alexhudson.com/2013/05/28/a-first-look-at-docker-io/>`_

* `Docker y el futuro de PaaS <https://blog.appfog.com/docker-and-the-future-of-the-paas-layer/>`_

* `Presentación docker <http://events.linuxfoundation.org/sites/events/files/slides/lcna13_petazzoni.pdf>`_

* `El futuro de docker <http://www.centurylinklabs.com/the-future-of-docker/?hvid=3hLgNz>`_

* `Presentación sobre Docker y maestro <http://es.slideshare.net/MaximePetazzoni/docker-and-maestro-for-fun-development-and-profit>`_

* `Montar volumenes solo para data <http://amattn.com/p/installing_maria_db_mysql_with_docker.html>`_

* `Montar volumenes solo para data <http://stackoverflow.com/questions/18496940/how-to-deal-with-persistent-storage-e-g-databases-in-docker>`_

* `Montar volumenes solo para data <http://www.tech-d.net/2013/12/16/persistent-volumes-with-docker-container-as-volume-pattern/>`_


.. _consul:

Consul
======

TODO
