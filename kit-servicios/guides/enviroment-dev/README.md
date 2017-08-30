# Guide to building the development environment

We define the steps one by one to be able to develop and test the application...

### 1 - Clone repository.

```
$ git clone http://gitlab.canaima.softwarelibre.gob.ve/canaima-gnu-linux/kit-servicios.git
```

### 2 - Positioning inside the cloned repository

```
$ cd kit-servicios
```

### 3 - Checkoit to branch development

``` 
$ git checkout development
```

### 4 -Install depends to develop

```
$ apt install virtualenv redis-server rabbitmq-server python-all-dev python-apt libffi-dev
```

### 5 - Create enviroment 

```
$ virtualenv <nombre del entorno>
```

### 7 - Activate enviroment

```
. <nombre del entorno>/bin/activate
```

### 8 - Positioning inside the cloned repository and install requirements:

```
$ pip install -r requirements.txt
```

### 9. Once finished to run kds we need to run several services that are celery, redis-server, rabbitmq-server and the django runserver


## Execute Redis

Execute in the terminal

```
$ redis-server
```

### Configure RabbitMQ for Celery ====

Antes de poder utilizar RabbitMQ para Ansible, tenemos que hacer algunas configuraciones para RabbitMQ. En pocas palabras, tenemos que crear una máquina virtual y un usuario y establecer permisos al usuario para que pueda acceder a la máquina virtual.

### add user 'kds' with password '11' ===

```
$ rabbitmqctl add_user kds 11
```

## add virtual host 'kds_vhost' 

```
$ rabbitmqctl add_vhost kds_vhost
```

## add user tag 'kds_tag' for user 'kds' 

```
$ rabbitmqctl set_user_tags kds kds_tag
```

## Set permission for user 'kds' on virtual host 'kds_vhost' 

```
$ rabbitmqctl set_permissions -p kds_vhost kds ".*" ".*" ".*"
```

## Run KDS

Positioning inside the cloned repository and execute:

```
python manage.py runserver
```

## Active the worker of Celery 

Open another terminal and repeat the step 7 and execute:

```
$ celery -A kds worker -P threads -l info
```


## 10. Check installation


Open with a browser the following url: ```http://127.0.0.1:8000/```
