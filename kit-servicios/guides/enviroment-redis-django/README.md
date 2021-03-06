# INSTALAR REDIS CON DJANGO


### 1 -  Instalar el server de redis:

```
sudo service redis-server start
```

### 2 - Check if Redis is up and accepting connections

```
$ redis-cli ping
```

Y la respuesta deberia ser PONG


### 3 - Install Django Websocket for Redis. The latest stable release can be found on PyPI


```
$ pip install django-websocket-redis
```

### 4 - Configurar el setting.py del proyecto de django

4.1 Add "ws4redis" to your project’s INSTALLED_APPS setting

```
INSTALLED_APPS = (
    ...
    'ws4redis',
    ...
)
```

4.2 Specify the URL that distinguishes websocket connections from normal requests

``` 
WEBSOCKET_URL = '/ws/'
```

4.3 Agregar la configuracion de conexion de redis

```
WS4REDIS_CONNECTION = {
    'host': 'redis.example.com',
    'port': 16379,
    'db': 17,
    'password': 'verysecret',
}
```

4.4 Especificar el tiempo que tardaran los mensajes en expirar

```
WS4REDIS_EXPIRE = 7200
```

4.5 Agregar un prefijo al websocket por donde se va acceder por defecto viene vacio.

```
WS4REDIS_PREFIX = 'ws'
```

4.6 Configuracion de wsgi esto es para desarrollo, esto es ignorado en produccion

```
WSGI_APPLICATION = 'ws4redis.django_runserver.application'
```

4.7 Agregar al TEMPLATE_CONTEXT_PROCESSORS estos procesadores:

```
TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'ws4redis.context_processors.default',
    ...
)
``` 

### 5. Configurar el archivo wsgi.py del proyecto

```
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kds.settings")

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

_django_app = get_wsgi_application()
_websocket_app = uWSGIWebsocketServer()

def application(environ, start_response):
    if environ.get('PATH_INFO').startswith(settings.WEBSOCKET_URL):
        return _websocket_app(environ, start_response)
    return _django_app(environ, start_response)
```


### 6 -  Añadir a las urls.py los staticfiles

```
from django.conf.urls import url, patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    ....
) + staticfiles_urlpatterns()
``` 

### 7 -  Agregar al archivo de configuracion de ngix la siguiente configuracion nginx.conf

```
server {
        
        location / {
   		include /etc/nginx/uwsgi_params;
	    	uwsgi_pass unix:/home/victor/Working/kit-servicios/kds/django.socket;
		}

		location /ws/ {
		    proxy_http_version 1.1;
		    proxy_set_header Upgrade $http_upgrade;
		    proxy_set_header Connection "upgrade";
		    proxy_pass http://unix/home/victor/Working/kit-servicios/kds/web.socket;
		    #proxy_pass http://localhost:6379;
		}
    }
``` 

### 8 - Dado que los dos manipuladores uWSGI crean su propio bucle principal, sino que también requieren su propia aplicación y diferentes conectores Unix. Crear dos archivos, uno para que adopte el bucle de Django:

Con nombre ```wsgi_django.py``` with the following content:

``` 
import os
os.environ.update(DJANGO_SETTINGS_MODULE='kds.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
``` 

And create the file for the loop WebSocket with the name  ```wsgi_websocket.py``` with the following content:

```
import os
import gevent.socket
import redis.connection
redis.connection.socket = gevent.socket
os.environ.update(DJANGO_SETTINGS_MODULE='kds.settings')
from ws4redis.uwsgi_runserver import uWSGIWebsocketServer
application = uWSGIWebsocketServer()
```

### 9. Hacer una notificacion a  Cada WebSocket conectado a un canal. foobar es el valor de referencia. (Este codigo colocarlo ya sea en una views).

```
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
message = RedisMessage('Hello World')
# and somewhere else
redis_publisher.publish_message(message)
``` 

### 10 - Hacer la peticion al websockets:

```
var ws = new WebSocket('ws://localhost:8000/ws/foobar?subscribe-broadcast&publish-broadcast&echo');

ws.onopen = function() {
    console.log("websocket connected");
};
ws.onmessage = function(e) {
    console.log("Received: " + e.data);
};
ws.onerror = function(e) {
    console.error(e);
};
ws.onclose = function(e) {
    console.log("connection closed");
}
function send_message(msg) {
    ws.send(msg);
}
```
