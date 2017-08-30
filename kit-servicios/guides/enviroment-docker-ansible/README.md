# Guide to test KDS wint Docker and Ansible

## 1 - Install Docker and Ansible

```
$ apt install docker.io ansible
```

## 2 - Download a image of debian to container

```
$ sudo docker pull debian:jessie
```

## 3 - Run the container

```
$ docker run -it debian:jessie
```

## 4 - Add the repositories:

```
$ echo "deb http://200.11.148.219/debian jessie main contrib non-free
deb http://200.11.148.219/seguridad jessie/updates main contrib non-free" > /etc/apt/sources.list
```

## 5 - Update

```
$ apt update
```

## 6 - Install packages to can work with the container

```
$ apt install nano python openssh-server sudo
```

## 7 - Create the user the container with the 

```
$ adduser kds
``` 

## 8. Login with su and create the folder ```.shh``` and the file ```authorized_keys```

``` 
$ su kds
$ mkdir .ssh
$ nano .ssh/authorized_keys
```

## 9 - Copy the key shh the master 

```
$ echo "llaveshh" > .ssh/authorized_keys
```

## 10 - Add the ip the container to file /etc/ansible/```hosts```

If you dont know the ip the container execute :

```
$ ip r 
```

Ok and now copy the content:

```
[kds]
192.168.101.104
```

## 11. Add user to sudoesr

```
$ echo "kds ALL=(ALL:ALL) ALL " >> /etc/sudoers
```

## 12. Active the service ssh

```
$ /etc/init.d/ssh start
```

## 13. Up the docker container

```bash
$ sudo docker start id
$ sudo docker attacth id
`` 
