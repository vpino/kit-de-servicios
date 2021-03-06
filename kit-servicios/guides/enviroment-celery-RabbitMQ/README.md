# Guide to Configuration Celery with RabbitMQ

###  Install Celery

```
$ pip install celery
```

### Install RabbitMQ

```
$ apt install rabbitmq-server
```

### Elegir un BROKER: RabbitMQ 


Aquí es donde comienza la confusión. ¿Por qué necesitamos otra cosa que se llama BROKER? Es porque ANSIBLE en realidad no consturuye una cola de mensajes en sí, por lo que necesita un transporte de mensaje adicional (un BROKER) para hacer ese trabajo. Se puede pensar en ANSIBLE como una envoltura alrededor de un intermediario de mensajes.

Estamos utilizando RabbitMQ como su BROKER, ya que es una característica-completo, estable y recomendado por ANSIBLE. 


### Configure RabbitMQ for Celery 

Antes de poder utilizar RabbitMQ para Ansible, tenemos que hacer algunas configuraciones para RabbitMQ. En pocas palabras, tenemos que crear una máquina virtual y un usuario y establecer permisos al usuario para que pueda acceder a la máquina virtual.


### add user 'kds' with password '11' 

```
$ rabbitmqctl add_user kds 11
``` 

### add virtual host 'kds_vhost' 

```
$ rabbitmqctl add_vhost kds_vhost
```

### add user tag 'kds_tag' for user 'kds' 

```
$ rabbitmqctl set_user_tags kds kds_tag
```

### set permission for user 'kds' on virtual host 'kds_vhost' 

```
$ rabbitmqctl set_permissions -p kds_vhost kds ".*" ".*" ".*"
```

## Hacer una instacia de celery para luego crear tareas ===

Ejemplo:

File ```celery.py``` with the following content

```python
from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://kds:11@localhost/kds_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])
```

### Argumentos de la instancia de Celery ====

1. El nombre del proyecto en el ejemplo 'test_celery'

2. El broker argumento que especifica la URL agente intermediario, que debe ser el que usa RabbitMQ. 

Tenga en cuenta que el formato para la url del BROKER debe ser:

```
transport://userid:password@hostname:port/virtual_host
```

For RabbitMQ, the transport is amqp.

3. BACKEND argumento especifica la URL para el back-end. Un back-end en ANSIBLE se utiliza para almacenar los resultados de la tarea. Así que si usted necesita tener acceso a los resultados de su tarea cuando esté terminada, debes configurarlo para ANSIBLE.

En este ejemplo se utilizo rpc para el backend que envia los resultados de vuelta en forma de mensajes AMQP, que es un formato aceptable para nuestra demostración. Más opciones para los formatos de mensaje se pueden encontrar aquí: 

http://docs.celeryproject.org/en/latest/configuration.html#std:setting-CELERY_RESULT_BACKEND

4. INCLUDE argunmento donde se especifica una lista de módulos que desea importar cuando ANSIBLE empiece a trabajar. Añadimos el módulo de tareas aquí para que el worker pueda encontrar nuestra tarea.


### File tasks.py 

En este archivo, nosotros definimos una tarea longtime_add:

```python
from __future__ import absolute_import
from test_celery.celery import app
import time

@app.task
def longtime_add(x, y):
    print 'long time task begins'
    # sleep 5 seconds
    time.sleep(5)
    print 'long time task finished'
    return x + y
```

Se puede ver que importamos la aplicación definida en el módulo anterior ANSIBLE y la utilizamos como decorador de nuestro método de trabajo. Tenga en cuenta que app.task es sólo un decorador. Además, dormimos 5 segundos nuestra tarea longtime_add para simular una tarea costosa en tiempo :)


### File run_tasks.py

Una vez configurado ANSIBLE, necesitamos ejecutar nuestra tarea, que se incluye en el ```runs_tasks.py```:

```python
from .tasks import longtime_add
import time

if __name__ == '__main__':
    result = longtime_add.delay(1,2)
    # at this time, our task is not finished, so it will return False
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result
```

Aquí, nosotros llamamos la tarea longtime_add utilizando el método de delay, el cual es necesario si queremos procesar la tarea asíncrona. Además, mantenemos los resultados de la tarea e imprimir algo de información. El método ready devolverá verdadero si la tarea se ha terminado, de lo contrario False. El metodo result deveulve el resultado de la tarea ("3" en nuestro caso). Si la tarea no se ha terminado, devuelve None.

### Ejecutar aplicacion de celery con python

create a file python ```main.py``` with the following  content:

```
from __future__ import absolute_import, unicode_literals
from celery import current_app
from celery.bin import worker

if __name__ == '__main__':
    app = current_app._get_current_object()

    worker = worker.worker(app=app)

    options = {
        'broker': 'amqp://guest:guest@localhost:5672//',
        'loglevel': 'INFO',
        'traceback': True,
    }

    worker.run(**options)
```
