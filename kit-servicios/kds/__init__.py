#from __future__ import absolute_import, unicode_literals
#from kds.celery import app
#from celery import current_app    
#from celery.bin import worker

#application = current_app._get_current_object()

#worker = worker.worker(app=application)

#options = {
#    'broker': 'amqp://kds:11@localhost/kds_vhost',
#    'loglevel': 'INFO',
#    'pool': 'threads',
#
#}

#worker.run(**options)