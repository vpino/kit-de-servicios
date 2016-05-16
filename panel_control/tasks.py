from __future__ import absolute_import
from common.ansible_manage import Runner
from kds.celery import app

@app.task
def add(x, y):

	data = [{'user': 'kds', 'passwd': '11'}]

	runner = Runner(
	hostnames='172.17.0.1',
	remote_user='kds',
	playbook='recetas/ansible-role-mailserver/site.yml',
	become_pass='11', 
	run_data=data,
	verbosity=1
	)

	stats = runner.run()

	return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)