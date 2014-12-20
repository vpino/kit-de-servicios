#!/usr/bin/env bash

#python manage.py celeryd -c 1 --beat -l INFO &
#python manage.py celery beat -s celerybeat-schedule &

celery -c 1 -A tribus.config.celery_cfg worker -l INFO &
python manage.py runserver 0.0.0.0:8000 

exit 0
