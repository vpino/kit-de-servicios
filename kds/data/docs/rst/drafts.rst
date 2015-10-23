=========================
Bitacora de Investigacion

https://blog.xenproject.org/2012/08/31/xen-tools-a-straightforward-vm-provisioninginstallation-tool/

http://www.scriptrock.com/blog/puppet-vs-cfengine

Tutoriales muy buenos de puppet:

- https://www.digitalocean.com/community/tutorials/how-to-configure-bind-as-a-private-network-dns-server-on-ubuntu-14-04
- https://www.digitalocean.com/community/tutorials/how-to-install-puppet-to-manage-your-server-infrastructure
- https://www.digitalocean.com/community/tutorials/getting-started-with-puppet-code-manifests-and-modules

Autometizar instalacion de Wordpress con Puppet:

- https://www.digitalocean.com/community/tutorials/how-to-create-a-puppet-module-to-automate-wordpress-installation-on-ubuntu-14-04

Ejemplo de uso de Hiera (Esto podria ser util construir los manifests personalizados):

- http://www.chriscowley.me.uk/blog/2013/04/11/using-hiera-with-puppet/


Otros enlaces de puppet que pueden ser utiles: 

- http://jamiei.com/blog/2011/12/cranking-up-the-dynamic-environments-with-puppet/

API de puppet:

- https://github.com/daradib/pypuppet
- https://docs.puppetlabs.com/guides/rest_api.html

Referencias de lenguaje puppet:

- https://docs.puppetlabs.com/learning/variables.html
- https://docs.puppetlabs.com/guides/style_guide.html

Buenas practicas con Ansible:

- http://hakunin.com/six-ansible-practices

Intro Ansible:

- http://tomoconnor.eu/blogish/getting-started-ansible/#.VRAhYvs4qV4
- https://serversforhackers.com/an-ansible-tutorial
- http://www.mechanicalfish.net/start-learning-ansible-with-one-line-and-no-files/
- https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-an-ubuntu-12-04-vps
- https://www.digitalocean.com/community/tutorials/how-to-create-ansible-playbooks-to-automate-system-configuration-on-ubuntu

Passwords en Ansible:

- http://serverfault.com/questions/560106/how-can-i-implement-ansible-with-per-host-passwords-securely
- http://stackoverflow.com/questions/21870083/specify-sudo-password-for-ansible


Provisionador de Vagrant para XenServer:

- https://github.com/jonludlam/vagrant-xenserver
- http://sharknet.us/2013/12/13/276/ (Usando Ansible)


Automatizacion de instalacion de Xen:

- http://xenapiadmin.com/tutorials/12-ubuntu-12-04-vm-64-bit-automated-preseed-installation-on-xcp


Configuracion de Xenapi: 

- https://help.ubuntu.com/community/Setting%20up%20Xen%20and%20XAPI%20(XenAPI)%20on%20Ubuntu%20Server%2012.04%20LTS%20and%20Managing%20it%20With%20Citrix%20XenCenter%20or%20OpenXenManager


Mas material de Ansible:

- https://adamcod.es/2014/09/23/vagrant-ansible-quickstart-tutorial.html
- http://docs.ansible.com/playbooks_variables.html#variables-defined-from-included-files-and-roles
- http://sharknet.us/2013/11/30/ansible-xen-vm-playbook/ (Usando ansible)

¿Cual es la diferencia entre XenServer y Xen Normal?

Solucion al problema de postfix que ya esta corriendo:

- http://serverfault.com/questions/54985/postfix-isnt-running-but-wont-start-because-the-postfix-mail-system-is-alread

Generar certificados de forma automatizada proveyendo los valores: 

- http://www.shellhacks.com/en/HowTo-Create-CSR-using-OpenSSL-Without-Prompt-Non-Interactive

Certificados Autofirmados:

- https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-apache-for-debian-7


Porque es necesario editar los roles de ansible para que no marquen los servicios como enabled al bootear::

- https://discourse.mailinabox.email/t/i-must-be-doing-something-wrong-spampd-error/155
- http://docs.ansible.com/service_module.html

En un contenedor no tengo systemd instalado y el enable en ansible parece hacer un llamado a systemd, por esto la conexion se "rompe" y muestra el error:

"""
msg: failure 1 running systemctl show for 'spamassassin.service': Failed to get D-Bus connection: Unknown error -1
"""

- https://workaround.org/ispmail/wheezy/webmail-roundcube
- https://www.howtoforge.com/using-roundcube-webmail-with-ispconfig-3-on-debian-wheezy-apache2

Tutorial de creacion de correo:

- http://www.xenlens.com/debian-wheezy-mail-server-postfix-dovecot-sasl-mysql-postfixadmin-roundcube-spamassassin-clamav-greylist-nginx-php5/

Excelente material para configurar roundcube en debian, solo esta un poco desfasado respecto a debian jessie:

- http://servidordebian.org/es/squeeze/email/webmail/roundcube

Ejemplos de virtualhosts en APACHE:

- https://wiki.apache.org/httpd/ExampleVhosts


Mas tutoriales para configurar Roundcube:

- https://workaround.org/ispmail/wheezy/webmail-roundcube (Instrucciones para configurar roundcube instalado desde los repositorios)
- http://www.cpierce.org/2012/04/roundcube-for-your-debian-squeeze-mail-server/
- http://wiki.canaima.softwarelibre.gob.ve/wiki/Instalación_y_Configuración_del_Webmail:Roundcube,_eGroupware_y_Mediawiki
- http://www.server-world.info/en/note?os=Debian_7.0&p=httpd&f=15
- http://www.debiantutorials.com/how-to-install-roundcube-on-squeeze/
- http://servidordebian.org/es/squeeze/email/webmail/roundcube
- https://www.howtoforge.com/using-roundcube-webmail-with-ispconfig-3-on-debian-wheezy-apache2
- http://ubuntuportal.com/2012/02/an-easy-step-by-step-to-installing-and-running-roundcube-webmail-on-ubuntu-linux-mint.html



Cambiar clave MYSQL:

- http://www.liquidweb.com/kb/change-a-password-for-mysql-on-linux-via-command-line/


Activar SSL en Apache:

- http://unix.stackexchange.com/questions/31378/apache2-invalid-command-sslengine

Tutorial de configuracion de dovecot y postfix que aparentemente funciona: 

- http://nksistemas.com/configurar-servidor-de-correo-en-debian-con-postfix-y-dovecot/


Tutorial montar servidor de correo postfix-dovecot:

- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-postfix-e-mail-server-with-dovecot



Otro tutorial aparentemente completo: 

- http://arstechnica.com/information-technology/2014/02/how-to-run-your-own-e-mail-server-with-your-own-domain-part-1/2/
- http://arstechnica.com/information-technology/2014/03/taking-e-mail-back-part-2-arming-your-server-with-postfix-dovecot/
- http://arstechnica.com/business/2014/03/taking-e-mail-back-part-3-fortifying-your-box-against-spammers/
- http://arstechnica.com/information-technology/2014/04/taking-e-mail-back-part-4-the-finale-with-webmail-everything-after/5/


echo 'Acquire::http::Proxy "http://10.16.106.139:8000";' > /etc/apt/apt.conf.d/30proxy 


Me quede sin Roundcube en testing: 

- https://tracker.debian.org/news/672271

Tutorial de servidor de correo completo en Gentoo:

- https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server

Comandos para ejecutar ansible-playbook:

ansible-playbook site.yaml -s --extra-vars '{"ansible_sudo_pass":"ola", "mailserver_dspam_mysql_password":"11", "mailserver_domain": "canaima.net.ve", "mailserver_fqdn": "kmail.canaima.net.ve"}' -u kds

Sobre el envio de correo desde un dominio distinto al dominio real:

- https://productforums.google.com/forum/#!topic/gmail/17EYTKyl7LM

Solucion BRUTAL para pasarle la clave a mysql al ejecutar un comando: 

- http://stackoverflow.com/questions/8055694/how-to-execute-a-mysql-command-from-a-shell-script


Error en la configuracion de postfix: 

- http://graysonpeddie.com/postfix-getting-helo-command-rejected-host-not-found/

Automatizacion de roundcube en ansible:

- https://github.com/marklee77/ansible-role-roundcube

Configuracion basica de postfix:

- http://www.postfix.org/BASIC_CONFIGURATION_README.html#relay_from

Migracion de correo imap:

- http://blog.phenobarbital.info/2015/02/migrando-correos-imap-usando-dovecot-imapsync-o-imapcopy/

Investigar estos plugins de ansible:

- https://github.com/ansible/ansible/tree/devel/plugins/inventory
Descripcion del error de recurso ocupado /etc/hosts cuando intento modificarlo en un script de ansible:

- https://github.com/docker/docker/issues/9295


ULTIMOS COMANDOS USADOS:

sudo ansible-playbook -s server.yaml -i /etc/ansible/consul_io.py --extra-vars '{"ansible_sudo_pass":"ola", "host":"local", "rol":"ansible-role-mailserver", "mailserver_dspam_mysql_password":"11", "mailserver_domain": "canaima.net.ve", "mailserver_fqdn": "kmail.canaima.net.ve"}' -u kds


Descripcion de un paquete (escrito en Perl) en OpenSUSE que hace lo que se espera en Kit de servicios: Crear, Listar y Destruir VM en XEN:

- https://software.opensuse.org/package/perl-Xen-API

Otro paquete similar: 

- https://software.opensuse.org/package/libxenserver2


Sobre como obtener feedback de las acciones realizadas en el servidor: 

- http://stackoverflow.com/questions/8096247/dynamic-pages-with-django-celery
- http://stackoverflow.com/questions/5479741/django-push-http-response-to-users

==========================================
Instalación de servicio de correo para KDS

Este manual fue construido utilizando las siguientes guias:

- http://www.xenlens.com/debian-wheezy-mail-server-postfix-dovecot-sasl-mysql-postfixadmin-roundcube-spamassassin-clamav-greylist-nginx-php5/
- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-postfix-e-mail-server-with-dovecot

===========================================================================
Instalacion de un servicio de correo local en un ambiente Debian Jessie/Sid

El dominio en este caso seria: canaima.net.ve

El subdominio seria: kmail.canaima.net.ve

En el archivo /etc/hosts hay que apuntar el subdominio a la ip del equipo donde se esta instalando el servidor de correo, ejemplo:

10.16.106.229	kmail.canaima.net.ve


====================================
Paquetes necesarios antes de empezar

apt-get install openssl


=============================================== 
Instalacion y configuracion de la base de datos

En este caso vamos a utilizar mysql como motor de base de datos para el servidor de correo, instalamos los siguientes paquetes:

apt-get install mysql-server mysql-client

Durante el proceso de instalacion nos debe salir un cuadro de dialogo solicitandonos que asignemos una constraseña para el usuario "root" (administrador). Colocamos nuestra contraseña de preferencia y continuamos. Esta constraseña es importante porque sera solicitada varias veces mas adelante

==========================================
1. Generacion de certificados autofirmados

Utilizando el siguiente comando se generan los certificados autofirmados:

/usr/bin/openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/ssl-cert-snakeoil.key -out /etc/ssl/certs/ssl-cert-snakeoil.pem -subj "/C=VE/ST=Caracas/L=Caracas/O=CNTI/OU=Proyecto Canaima/CN=jsfrncscg@gmail.com"

==========
2. Postfix

=====================
2.1 Instalar paquetes

apt-get install postfix

Durante la instalacion se nos preguntara el tipo de configuracion para el servicio de correo, aqui vamos a seleccionar la opcion "Internet Site". Luego nos pedira el nombre de nuestro sub-dominio de correo, en este caso colocamos 'kmail.canaima.net.ve'

======================
2.2 Configurar postfix

En el archivo "/etc/postfix/master.cf" se debe descomentar de manera que la seccion "submission inet" quede de esta forma:

submission inet n       -       -       -       -       smtpd
  -o syslog_name=postfix/submission
  -o smtpd_tls_wrappermode=no
  -o smtpd_tls_security_level=encrypt
  -o smtpd_sasl_auth_enable=yes
  -o smtpd_recipient_restrictions=permit_mynetworks,permit_sasl_authenticated,reject
  -o milter_macro_daemon_name=ORIGINATING
  -o smtpd_sasl_type=dovecot
  -o smtpd_sasl_path=private/auth


En el archivo "/etc/postfix/main.cf" es importante que las siguientes configuraciones queden como se muestra a continuacion:


myhostname = kmail.canaima.net.ve
myorigin = /etc/mailname
mydestination = kmail.canaima.net.ve, canaima.net.ve, localhost, localhost.localdomain
relayhost =
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all

alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases

smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
smtpd_use_tls=yes
smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache
smtpd_tls_security_level=may
smtpd_tls_protocols = !SSLv2, !SSLv3

====================
2.3 Actualizar alias

Ejecutar el comando 'newaliases'

==========
3. Dovecot

===========================
3.1 Instalacion de paquetes

apt-get install dovecot-core dovecot-imapd

======================
3.2 Configurar dovecot

Abrir el archivo "/etc/dovecot/dovecot.conf" y borrar TODO su contenido. A continuación el nuevo contenido que tendra el archivo:


disable_plaintext_auth = no
mail_privileged_group = mail
mail_location = mbox:~/mail:INBOX=/var/mail/%u

userdb {
  driver = passwd
}

passdb {
  args = %s
  driver = pam
}

protocols = " imap"

# >>>> Esta configuracion esta obsoleta, debo buscar como actualizarla
protocol imap {
  mail_plugins = " autocreate"
}

plugin {
  autocreate = Trash
  autocreate2 = Sent
  autosubscribe = Trash
  autosubscribe2 = Sent
}

# <<<<< Fin Configuracion obsoleta

service auth {
  unix_listener /var/spool/postfix/private/auth {
    group = postfix
    mode = 0660
    user = postfix
  }
}

ssl=required
ssl_cert = </etc/ssl/certs/ssl-cert-snakeoil.pem
ssl_key = </etc/ssl/private/ssl-cert-snakeoil.key

====================
4. Iniciar servicios

Ejecutar los siguientes comandos para inciar los servicios

newaliases
postfix start
service dovecot restart


==========================
5. Instalar otros paquetes

Otros paquetes que necesitaremos instalar:

apt install apache2 postfixadmin roundcube

tanto postfixadmin como roundcube pediran la clave de root de mysql generada anteriormente en el paso X, luego se asignara una clave para el usuario postfix y el usuario roundcube


==========================
6. Configurar postfixadmin


==================================
6.1 Crear tablas para postfixadmin


Nos logeamos en el cliente de mysql y procedemos a crear las tablas y asignar los permisos correspondientes:

CREATE DATABASE postfix;
GRANT ALL PRIVILEGES ON postfix.* TO 'postfix_admin'@'%' IDENTIFIED BY '11';
GRANT SELECT ON postfix.* TO 'postfix'@'%' IDENTIFIED BY '11';
FLUSH PRIVILEGES;

====================================
6.2 Editar archivos de configuracion

En este punto la direccion "kmail.canaima.net.ve/postfixadmin" deberia estar disponible y mostrar una pantalla de login para el administrador del sistema, pero antes vamos a configurar postfixadmin, para ello nos dirigimos a "kmail.canaima.net.ve/postfixadmin/setup.php"

en esta pagina se nos solicita que asignemos una clave administrativa para postfix, colocamos la clave y le damos a 'generate password hash', seguidamente la pagina nos indica el hash generado, debemos copiar este hash en el archivo de configuracion '/etc/postfixadmin/config.inc.php' en la opcion:

$CONF['setup_password'] = 'changeme';

debe quedar algo similar a esto:

$CONF['setup_password'] = '2abd6472c1cfa53ff11bffd667eadc98:fa8da49f7ecb8bebf9afd823a506bdbc192f2b6a';

otras opciones de configuración que nos interesan son los parametros de conexion con la base de datos:

$CONF['database_type'] = 'mysqli';
$CONF['database_host'] = 'localhost';
$CONF['database_user'] = 'postfix_admin';
$CONF['database_password'] = '11';
$CONF['database_name'] = 'postfix';

otras opciones de configuracion:

$CONF['domain_path'] = 'YES';

$CONF['domain_in_mailbox'] = 'NO';

$CONF['fetchmail'] = 'NO';

guardamos y cerramos el archivo. Ahora volvemos a la pagina donde quedamos y creamos la cuenta de administrador. Si todo esta correcto, nos notificara que la cuenta fue creada y podremos acceder a ella en la dirección: 'kmail.canaima.net.ve/postfixadmin', nos logueamos y ya podramos registrar dominios y crear buzones de correo.

========================
6.3 Registrar el dominio

Una vez logueados con la cuenta de administrador en postfix admin, buscamos la opcion 'nuevo dominio', click alli y procedemos a registrar el dominio 'canaima.net.ve'. 

=====================
6.4 Registrar buzones

Buscamos la opcion 'añadir buzon' y alli registramos a los usuarios con los que deseamos acceder. 



=======================
7. Configurar roundcube


Primero se edita el archivo "/etc/apache2/conf-available/roundcube.conf", alli descomentaremos las siguientes lineas:

#    Alias /roundcube/program/js/tiny_mce/ /usr/share/tinymce/www/
#    Alias /roundcube /var/lib/roundcube

con esto es suficiente para poder acceder a roundcube desde la direccion "kmail.canaima.net.ve/roundcube"

Seguidamente editamos el archivo "/etc/roundcube/main.inc.php", alli nos interesa que las siguientes opciones queden asi: 

$rcmail_config['language'] = 'es_ES';

$rcmail_config['default_host'] = 'canaima.net.ve';

$rcmail_config['smtp_server'] = 'localhost';

reiniciamos apache para que los cambios tengan efecto:

service apache2 restart

==========================
Estado actual del proyecto

F.A.Q

¿Porque estan utilizando Ansible en lugar de <Herramienta de configuracion X>?

¿Cuales son los requerimientos no funcionales?

En el caso de la plataforma de virtualización se requiere una herramienta que cumpla con los siguientes aspectos:

- Automatizable: debe ser posible crear nuevas instancias de maquinas virtuales/contenedores de manera desasistida, sin necesidad de interrumpir su creación para solicitar datos como contraseñas, etc. Lo ideal seria que los datos mas relevantes de la configuración basica de la VM/Contenedor puedan pre-sembrarse y que al momento de constuirla se tomen esos valores y se asignen.

- Las VM/Contenedores generados deben tener una IP Fija: Aun no tengo evidencia de que esto sea estrictamente necesario, sin embargo considero importante que una vez se crea una VM/Contenedor esta mantenga la misma dirección IP dentro de la red interna del Servidor, de manera que sea mas facil localizarla al momento de consultar su estado, actualizar su configuración o realizar algun otro tipo de operación sobre ella.

- La plataforma de virtualización debe estar empaquetada en Debian Jessie: Esto es importante dado que si la plataforma de virtualización no esta empaquetada en la version estable de debian seria necesario empaquetarla (al igual que mantenerla durante un periodo de tiempo prolongado) o instalarla utilizando algun mecanismo no convencional. Las experiencias anteriores con estas soluciones (empaquetandolas o instalandolas por vias alternativas) no han generado resultados satisfactorios y en la mayoria de los casos han sido mas los problemas que acarrean que el problema que solucionan.

Obstaculos para la adopción de Xen como plataforma de virtualización:

- No he encontrado indicios de que pueda automatizar completamente (es discutible si es necesario que sea completamente automatizado) el proceso de creación de una maquina virtual. Hay algunos aspectos de los cuales no hay información clara o requieren intervención del usuario, como presembrar la contraseña de root de la maquina virtual. Necesito mas investigacion en esta area para poder aportar datos o hechos concretos.

- Algunos paquetes considerados para manejar el dom0 del servidor son: xcp-api y python-xenapi (ambos construidos por el mismo paquete fuente). Desafortunadamente estos paquetes solo estan disponibles en la versión 7.0 de Debian (Wheezy/Old-Stable). Mas detalles sobre la configuracion de Xenapi: https://help.ubuntu.com/community/Setting%20up%20Xen%20and%20XAPI%20(XenAPI)%20on%20Ubuntu%20Server%2012.04%20LTS%20and%20Managing%20it%20With%20Citrix%20XenCenter%20or%20OpenXenManager

¿Que tenemos de Kit de Servicios hasta el momento?

Un paquete que instala la interfaz administrativa (Nginx + uwsgi + Django + Plugins). Hasta el momento la interfaz administrativa solo muestra una lista que contiene un solo servicio (mediawiki). Este puede arrastrarse hasta el canvas y alli se proporcionan los datos de login (usuario y contraseña) del usuario privilegiado, es decir aquel autorizado en el servidor para realizar las operaciones de despliegue de servicios.

Utilizando el modulo sudo de fabric es posible ejecutar tareas en el servidor que requieren permisos de root. (La creación del usuario privilegiado queda de parte del administrador del sistema). De esta forma se pueden ejecutar tareas en donde se maneja el demonio que controla a la plataforma de virtualización o al orquestador, pasandole a estos ultimos los parametros recibidos desde la interfaz administrativa.

Un parche en el codigo de ansible para que ignore aquellos nodos en los que no se detecta ningun servicio corriendo.

Un plugin adaptado a partir de: https://github.com/ansible/ansible/blob/devel/plugins/inventory/docker.py que permite consultarle al demonio de docker sobre el estado de los contenedores que estan corriendo actualmente.

