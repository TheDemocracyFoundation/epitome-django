#!/bin/bash

source ~/EpitomeVE/bin/activate 

pip install gunicorn psycopg2 

cd ~/Epitome 

EXTERNALIP="$(curl ipinfo.io/ip)"

sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ['$EXTERNALIP']/" ~/Epitome/Epitome/settings.py

gunicorn --bind $EXTIP:8000 Epitome.wsgi
