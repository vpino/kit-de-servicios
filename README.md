# Kit de Servicios

![Travis Test](https://travis-ci.org/vpino/kit-de-servicios.svg?branch=master "Travis") 

![Requires Test](https://requires.io/github/vpino/kit-de-servicios/requirements.svg?branch=master "requires") 

![Quantifiedcode Test](https://www.quantifiedcode.com/api/v1/project/996b4cefb3074a258fa9df95bff84df6/badge.svg "Quantifiedcode") 

![Landscape Test](https://landscape.io/github/vpino/kit-de-servicios/master/landscape.svg?style=flat "Landscape") 

![Coveralls Test](https://coveralls.io/repos/github/vpino/kit-de-servicios/badge.svg?branch=master "Coveralls") 


# Integrar Receta a Kit de Servicios

Para integrar una receta se deben cumplir unos requisitos y una estructura. Ademas unos cumplidos los mismos, deben realizarce unos pasos especificos, los cuales seran explicados mas adelante.

## Requisitos de la Receta

* La receta debe ser compatible con la versión de ansible 2.0.0 o superior.
* La receta debe contener contener un CRUD (pasos de instalación, actualización, eliminación y consulta).
* El nombre de la receta debe seguir la siguiente nomenclatura:
> ansible-role-<nombre_receta>

Ejemplo: ansible-role-mailserver


## Estructura de directorios de la Receta

La receta debe estar compuesta con la siguiente estructura:

```bash
Nombre_receta ├── 
              ├── group_vars
                 ├── all
              ├──  handlers
                 ├── main.yml
              ├── meta
                 ├── main.yml
              ├── roles
                 ├──  role1
                 ├──  role2
              ├── README.md
              ├──  site.yml
			  ├── Nombre_receta
			     ├── metadata.json
			     ├── config.json
```

El directorio que se cuentra dentro de la ``receta`` con el mismo nombre que la ``receta``, contiene toda la informacion que necesita KDS para hacer funcionar la  ``receta``. El cual suministra 2 archivos:


> 1.- ``metadata.json`` Contiene la información generica de la receta. Con la siguiente estructura:

```bash
[
	{
	"name": "",
	"summary": "",
	"maintainer": "",
	"description": ""
	}
]
```

### Ejemplo:

```json
[
	{
	"name": "correo",
	"summary": "Servicio de correo",
	"maintainer": "Victor Pino <victopin0@gmail.com>",
	"description": "Un servidor de correo es una aplicación de red de computadoras ubicada en un servidor de Internet, para prestar servicio de correo electrónico (correo-e o e-mail). El Mail Transfer Agent (MTA) tiene varias formas de comunicarse con otros servidores de correo: Recibe los mensajes desde otro MTA. Actúa como SERVIDOR de otros servidores. Envía los mensajes hacia otro MTA. Actúa como un CLIENTE de otros servidores. Actúa como intermediario entre un Mail Submission Agent y otro MTA."
	}
]
```

> 2.- ```config.json``` Contiene la información especifica de las variables declaradas en la receta. En este archivo se detalla en que paso del CRUD sera utilizada una variable, si es en la instalación, actualización etc.

Estructura del archivo:

```json

{
  "install": 
  [

    {
      "name": "",
      "label": "",
      "default": "",
      "tooltip": "",
      "type": ""
    }

  ],

  "update": 

  {
    "modules": 
    [

      {

        "<name-module>": 
        [

          {
            "name": "",
            "label": "",
            "default": "",
            "tooltip": "",
            "type": ""
          }

        ]

      }

    ]

  },

  "query": 
  [
    {
      "service": "",
      "package": "",
      "description": "
    }

  ],

  "message_success": "",

  "after_installing": ""

}
```
 
### Ahora generemos un archivo ```config.json``` real paso a paso


> 1.- Crear el archivo

```json
$ touch config.json
```

> 2.- Iniciar el json:

```json
{


}
```

> 3.- Añadir las variables que seran usadas en la instalación de la receta, para esto añadimos la clave ```"install":``` que tiene como valor una lista ```[]``` de diccionarios ```{}```

```json
{
  
  "install":
  [
    {

    }
  ]

}
```

> 3.1 Ok, ahora añadimos la informacion de nuestras variables que seran usadas en la instalación.

```json
{
  
  "install":
  [
    {
      "name": "mailserver_domain",
      "label": "Dominio del Correo",
      "default": "canaima.net.ve",
      "tooltip": "Dominio a cual se hara referencia. ejemplo: gmail.com",
      "type": "String"
    },

    {
      "name": "mailserver_fqdn",
      "label": "FQDN",
      "default": "kmail.canaima.net.ve",
      "tooltip": "Nombre dominio completo del servicio de correo",
      "type": "String"
    }
  ]

}
```

#### OK expliquemos el contenido del diccionario ```{}```

* ```name```: Su valor es, el nombre de la variable.
* ```label```: Su valor es, la etiqueta que quieres que aparesca en el campo del formulario en la interfaz web.
* ```default```: El valor por default de la variable.
* ```tooltip```: Descripción emergente, referente a la variable.
* ```type```: El tipo de la variable.


> 4.- Ahora añadimos las variables que van hacer usadas en la actulizacion. Pero antes el paso de actualizacion puede estar dividido en modulos, por ejemplo un modulo de actualizacion para agregar usuario como tambien un modulo de actualizacion para eliminar usuarios.

### OK manos a la obra primero creamos la clave update: el cual contiene un diccionario.

```json
{
  
  "install":
  [
    {
      "name": "mailserver_domain",
      "label": "Dominio del Correo",
      "default": "canaima.net.ve",
      "tooltip": "Dominio a cual se hara referencia. ejemplo: gmail.com",
      "type": "String"
    },

    {
      "name": "mailserver_fqdn",
      "label": "FQDN",
      "default": "kmail.canaima.net.ve",
      "tooltip": "Nombre dominio completo del servicio de correo",
      "type": "String"
    }
  ],

  "update":
  {

  }

}
```


### Ahora este diccionario contiene una clave llamada ```modules``` la cual contiene a su ves una lista ```[]``` de diccionarios ```{}```:


```json
{
  
  "install":
  [
    {
      "name": "mailserver_domain",
      "label": "Dominio del Correo",
      "default": "canaima.net.ve",
      "tooltip": "Dominio a cual se hara referencia. ejemplo: gmail.com",
      "type": "String"
    },

    {
      "name": "mailserver_fqdn",
      "label": "FQDN",
      "default": "kmail.canaima.net.ve",
      "tooltip": "Nombre dominio completo del servicio de correo",
      "type": "String"
    }
  ],

  "update":
  {
    "modules":
    [

      {

      }

    ]
  }

}
```

### Ahora añadimos los modulos que tendra nuestro apartado de actualizacion creando un diccionario por cada variable que contenga este modulo:


```json
{
  
  "install":
  [
    {
      "name": "mailserver_domain",
      "label": "Dominio del Correo",
      "default": "canaima.net.ve",
      "tooltip": "Dominio a cual se hara referencia. ejemplo: gmail.com",
      "type": "String"
    },

    {
      "name": "mailserver_fqdn",
      "label": "FQDN",
      "default": "kmail.canaima.net.ve",
      "tooltip": "Nombre dominio completo del servicio de correo",
      "type": "String"
    }
  ],

  "update":
  {
    "modules":
    [

      {
      "Agregar-Usuario": 

          [

            {
              "name": "user",
              "label": "Direccion de correo",
              "default": "",
              "tooltip": "Nombre del correo",
              "type": "String"
            },

            {
              "name": "passwd",
              "label": "Contraseña",
              "default": "",
              "tooltip": "Contraseña del correo",
              "type": "Password"
            }


          ]

      }

    ]
  }

}
```

Ahora si se fijan creamos el modulo ```"Agregar-Usuario":``` el cual es una llave que contiene una lista ```[]``` de diccionarios ```{}```. A lo cual cada diccionario corresponde a una variable con toda su información

### Ok fino ahora agreguemos el otro modulo que nos falta:

```json
{
  
  "install":
  [
    {
      "name": "mailserver_domain",
      "label": "Dominio del Correo",
      "default": "canaima.net.ve",
      "tooltip": "Dominio a cual se hara referencia. ejemplo: gmail.com",
      "type": "String"
    },

    {
      "name": "mailserver_fqdn",
      "label": "FQDN",
      "default": "kmail.canaima.net.ve",
      "tooltip": "Nombre dominio completo del servicio de correo",
      "type": "String"
    }
  ],

  "update":
  {
    "modules":
    [

      {
      "Agregar-Usuario": 

          [

            {
              "name": "user",
              "label": "Direccion de correo",
              "default": "",
              "tooltip": "Nombre del correo",
              "type": "String"
            },

            {
              "name": "passwd",
              "label": "Contraseña",
              "default": "",
              "tooltip": "Contraseña del correo",
              "type": "Password"
            }


          ]

      },

      {
        Eliminar-Usuario": 
        [

          {
            "name": "user",
            "label": "Direccion de correo",
            "default": "",
            "tooltip": "Nombre del correo",
            "type": "String"
          },

          {
            "name": "passwd",
            "label": "Contraseña",
            "default": "",
            "tooltip": "Contraseña del correo",
            "type": "Password"
          }

        ]

      }

    ]

  }

}
```


Ok fino terminado el apartado de actualización de la receta


### Ahora vamos añadir el apartado de consulta


Añadimos la clave ```"update"``` la cual tiene como valor una lista de diccionarios

```json
{
  
  "install":
  [
    {
      "name": "mailserver_domain",
      "label": "Dominio del Correo",
      "default": "canaima.net.ve",
      "tooltip": "Dominio a cual se hara referencia. ejemplo: gmail.com",
      "type": "String"
    },

    {
      "name": "mailserver_fqdn",
      "label": "FQDN",
      "default": "kmail.canaima.net.ve",
      "tooltip": "Nombre dominio completo del servicio de correo",
      "type": "String"
    }
  ],

  "update":
  {
    "modules":
    [

      {
      "Agregar-Usuario": 

          [

            {
              "name": "user",
              "label": "Direccion de correo",
              "default": "",
              "tooltip": "Nombre del correo",
              "type": "String"
            },

            {
              "name": "passwd",
              "label": "Contraseña",
              "default": "",
              "tooltip": "Contraseña del correo",
              "type": "Password"
            }


          ]

      },

      {
        Eliminar-Usuario": 
        [

          {
            "name": "user",
            "label": "Direccion de correo",
            "default": "",
            "tooltip": "Nombre del correo",
            "type": "String"
          },

          {
            "name": "passwd",
            "label": "Contraseña",
            "default": "",
            "tooltip": "Contraseña del correo",
            "type": "Password"
          }

        ]

      }

    ]

  },

  "query":

  [
    {
      "service": "postfix",
      "package": "postfix",
      "description": "Es un servidor de correo"
    },

    {
      "service": "dovecot",
      "package": "dovecot-imapd",
      "description": "Es un servidor de IMAP y POP3"
    }

  ],

}
```

### OK expliquemos este apartado

Este apartado tiene como fin consultar el estado de los servicios de tu receta y en el cual nos basaremos para saber si esta instalado o no la receta.


OK para esto se define un diccionario con la siguiente información:

>
* "service": Nombre del servicio, al cual se hace referencia en el demonio para poder ya sea reiniciar, iniciarlo. Ejemplo ```/etc/init/postfix status```.

* "package": Nombre del paquete por cual se sabe que el servicio esta instaldo.

* "description": La descripción del servicio.

Un ejemplo real:

```json
{
  "service": "dovecot",
  "package": "dovecot-imapd",
  "description": "Es un servidor de IMAP y POP3""
}
```


### Ok listo con esto ya tenemos casi listo nuestro archivo ```config.json```.

Ahora lo que nos falta es agregarlo 2 llaves mas que corresponde:

> * "message_success" Esta llave tiene como función imprimir un mensaje, cuando la instalación sea exitosa.

### Ejemplo:

```json
"message_success": "Dirigirse a la siguiente ruta para verificar la instalacion del servico localhost/squirrelmail/ ",
```

> * "after_installing": Esta llave permite imprimir otro mensaje, luego de que la instalacion finalice 

### Ejemplo:

```json
"after_installing": "Debera crear un Usuario con el modulo de actualización de la aplicación"
``` 

### Ok con esto claro procedamos a añadir las variables a nuestro ```config.json```.

```json
{
  
  "install":
  [
    {
      "name": "mailserver_domain",
      "label": "Dominio del Correo",
      "default": "canaima.net.ve",
      "tooltip": "Dominio a cual se hara referencia. ejemplo: gmail.com",
      "type": "String"
    },

    {
      "name": "mailserver_fqdn",
      "label": "FQDN",
      "default": "kmail.canaima.net.ve",
      "tooltip": "Nombre dominio completo del servicio de correo",
      "type": "String"
    }
  ],

  "update":
  {
    "modules":
    [

      {
      "Agregar-Usuario": 

          [

            {
              "name": "user",
              "label": "Direccion de correo",
              "default": "",
              "tooltip": "Nombre del correo",
              "type": "String"
            },

            {
              "name": "passwd",
              "label": "Contraseña",
              "default": "",
              "tooltip": "Contraseña del correo",
              "type": "Password"
            }


          ]

      },

      {
        Eliminar-Usuario": 
        [

          {
            "name": "user",
            "label": "Direccion de correo",
            "default": "",
            "tooltip": "Nombre del correo",
            "type": "String"
          },

          {
            "name": "passwd",
            "label": "Contraseña",
            "default": "",
            "tooltip": "Contraseña del correo",
            "type": "Password"
          }

        ]

      }

    ]

  },

  "query":

  [
    {
      "service": "postfix",
      "package": "postfix",
      "description": "Es un servidor de correo"
    },

    {
      "service": "dovecot",
      "package": "dovecot-imapd",
      "description": "Es un servidor de IMAP y POP3"
    }

  ],

  "message_success": "Dirigirse a la siguiente ruta para verificar la instalacion del servico localhost/squirrelmail/ ",

  "after_installing": "Debera crear un Usuario con el modulo de actualización de la aplicación"

}
```

Y con esto tenemos nuestra receta integrada a ```kit de servicios```.