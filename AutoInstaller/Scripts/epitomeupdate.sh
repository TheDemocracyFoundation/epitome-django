#!/bin/bash

mkdir ~/tempepitome

cd ~/tempepitome

git clone https://github.com/TheDemocracyFoundation/epitome.git

cd ~/tempepitome

git checkout development

source ~/EpitomeVE/bin/activate

cd ~/tempepitome

cp -rf * ~/Epitome

rm -rf ~/tempepitome

cd ~/Epitome

python3 manage.py makemigrations Demoscopesis

python3 manage.py makemigrations Agora

python3 manage.py makemigrations Propylaea

python3 manage.py migrate
