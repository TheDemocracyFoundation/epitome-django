#!/bin/bash

source ~/EpitomeVE/bin/activate 

pip install gunicorn psycopg2 

cd ~/Epitome 

EXTIP="$(curl ipinfo.io/ip)"

sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ['$EXTIP']/" ~/Epitome/Epitome/settings.py

gunicorn --bind $EXTIP:8000 Epitome.wsgi
