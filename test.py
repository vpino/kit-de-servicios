import os
import json
from tribus import BASEDIR
from tribus.common.utils import get_path
from tribus.common.recipes.recipe import RecipeDir
from tribus.common.schema import *
from tribus.config.base import CHARMSDIR, SERVICEDIR

# test_path = get_path([BASEDIR, 'tribus', 'data', 'services', 'wiki'])

# cfg = json.load(open(os.path.join(CHARMSDIR, 'mysql', 'config', 'app.json')))

# rd = RecipeDir(test_path)

# print rd.metadata.name
# print rd.metadata.description
# print rd.metadata.components.items()

# print cfg['service']['port']


from fabric.api import env, sudo, quiet, execute
from tribus.common.fabric.consul import deploy_test_service

env.port = 22
env.user = 'fran'
env.password = '11'
env.host_string = '192.168.0.106'
env.service_name = 'wiki'

execute(deploy_test_service)









