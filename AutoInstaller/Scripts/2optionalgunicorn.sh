#!/bin/bash

source ~/EpitomeVE/bin/activate

pip install gunicorn psycopg2

cd ~/Epitome

EXTERNALIP="$(curl ipinfo.io/ip)"

symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 EPITOME_SECRET_KEY=; for (( i = 0; i < length; i++ )); do EPITOME_SECRET_KEY+=${symbols[RANDOM%${#symbols[@]}]}; done; export EPITOME_SECRET_KEY

sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ['$EXTERNALIP','localhost']/" ~/Epitome/Epitome/settings.py

gunicorn --bind $EXTERNALIP:8000 Epitome.wsgi
