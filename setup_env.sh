#!/bin/sh

activate () {
  . ../venv/bin/activate
}

sudo apt install python-dev libxml2-dev libxslt1-dev libsasl2-dev libldap2-dev libpq-dev gcc python-pip 

PROJECT_PATH=$(pwd)
cd ..
ROOT=$(pwd)
cd $PROJECT_PATH

virtualenv ../venv

activate

sudo pip install pip2pi

pip2tgz ../packages/ -r req.txt

pip install --index-url=file://$ROOT/packages/simple  -r req.txt
