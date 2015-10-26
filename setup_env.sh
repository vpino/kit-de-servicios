#!/bin/sh

activate () {
  . ../venv/bin/activate
}

sudo apt install python-dev libxml2-dev libxslt1-dev libsasl2-dev libldap2-dev libpq-dev gcc

PROJECT_PATH=$(pwd)
cd ..
ROOT=$(pwd)
cd $PROJECT_PATH

virtualenv ../venv

activate

pip2tgz ../packages/ -r req.txt

pip install --index-url=file://$ROOT/packages/simple  -r req.txt
