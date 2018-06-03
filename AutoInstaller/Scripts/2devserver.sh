#!/bin/bash

source ~/EpitomeVE/bin/activate

cd ~/Epitome

sed -i "s/DEBUG = False/DEBUG = True/" ~/Epitome/Epitome/settings.py

python3 manage.py runserver
