#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

NAME = 'Kit de servicios'
VERSION = (0, 1, 17, 'alpha', 1)
URL = 'http://gitlab.canaima.softwarelibre.gob.ve/canaima-gnu-linux/kit-servicios/'
AUTHOR = 'Victor Pino'
AUTHOR_EMAIL = 'victopin0@gmail.com'
DESCRIPTION = ('Automatización y despliegue de servicios para la AP.')
LICENSE = 'GPL'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICEDIR = BASE_DIR + '/data/services'
RECIPESDIR = BASE_DIR + '/common/recetas'
SSHDIR = '/home/kds/.ssh/id_rsa.pub'
RECI_CONFIG = 'config.json'
