#!/bin/sh

# http://stackoverflow.com/questions/12521552/installing-pip-packages-to-a-virtualenv-using-a-download-cache

activate () {
  . ../venv/bin/activate
}

 

sudo apt install nmap python-pip python-dev libxml2-dev libxslt1-dev libsasl2-dev libldap2-dev libpq-dev gcc rabbitmq-server
               

PROJECT_PATH=$(pwd)
cd ..
ROOT=$(pwd)
cd $PROJECT_PATH

virtualenv ../venv

activate


sudo pip install pip2pi




pip2tgz ../packages/ -r req.txt

dir2pi -n ../packages

pip install --index-url=file://$ROOT/packages/simple  -r req.txt
