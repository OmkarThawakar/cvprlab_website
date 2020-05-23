#!/bin/bash

NAME="cvprlab"                              #Name of the application (*)
DJANGODIR=/var/www/html/cvprlab_website             # Django project directory (*)
USER=ubuntu                                        # the user to run as (*)
GROUP=www-data                                     # the group to run as (*)
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=CVPRLab.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=CVPRLab.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/ubuntu/Envs/django/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/ubuntu/Envs/django/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--user $USER \
	--config ${DJANGODIR}/CVPRLab/gunicorn_config.py
