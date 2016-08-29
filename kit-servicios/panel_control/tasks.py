from __future__ import absolute_import
from common.ansible_manage import Runner
from kds.celery import app
from common.tail_f import TailLog
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.task
def add(hostnames, remote_user, playbook, become_pass, run_data, verbosity):

	runner = Runner(
        hostnames=hostnames,
        remote_user=remote_user,
        playbook=playbook,
        become_pass=become_pass, 
        run_data=run_data,
        verbosity=verbosity
        )

	stats = runner.run()

	return stats

@app.task
def tail_logger():

        tail = TailLog(BASE_DIR+"/", 'playbook-log')

        return 'ok'

