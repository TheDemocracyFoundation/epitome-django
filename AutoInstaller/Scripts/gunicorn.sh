#!/bin/bash

source ~/EpitomeVE/bin/activate 

pip install gunicorn psycopg2 

cd ~/Epitome 

gunicorn --bind 0.0.0.0:8000 Epitome.wsgi
