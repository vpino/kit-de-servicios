from __future__ import absolute_import
from common.ansible_manage import Runner
from kds.celery import app

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

        print stats 

	return stats

