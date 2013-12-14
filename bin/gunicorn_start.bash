#!/bin/bash

NAME="rz"                                  # Name of the application
DJANGODIR=/home/mrisher/src/apps/rz            # Django project directory
SOCKFILE=/home/mrisher/src/apps/rz/run/gunicorn.sock  # we will communicte using this unix socket
USER=rz                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=rz.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=rz.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=debug \
  --bind=unix:$SOCKFILE
