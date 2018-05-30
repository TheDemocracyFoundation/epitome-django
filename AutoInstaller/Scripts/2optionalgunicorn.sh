#!/bin/bash

source ~/EpitomeVE/bin/activate 

pip install gunicorn psycopg2 

cd ~/Epitome 

EXTIP="$(curl ipinfo.io/ip)"

gunicorn --bind $EXTIP:8000 Epitome.wsgi
