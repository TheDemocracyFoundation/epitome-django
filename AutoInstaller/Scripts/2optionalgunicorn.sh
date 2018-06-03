#!/bin/bash

source ~/EpitomeVE/bin/activate

pip install gunicorn psycopg2

cd ~/Epitome

EXTERNALIP="$(curl ipinfo.io/ip)"

sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ['$EXTERNALIP','localhost']/" ~/Epitome/Epitome/settings.py

sed -i "s/DEBUG = True/DEBUG = False/" ~/Epitome/Epitome/settings.py

gunicorn --bind $EXTERNALIP:8000 Epitome.wsgi
