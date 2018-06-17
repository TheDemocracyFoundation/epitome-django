#!/bin/bash
echo 'In order to create a administrator account, please provide the following information:'
echo    # move to a new line

source ~/EpitomeVE/bin/activate 

cd ~/Epitome 

python3 manage.py createsuperuser
