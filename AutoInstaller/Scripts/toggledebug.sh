#!/bin/bash

source ~/EpitomeVE/bin/activate

cd ~/Epitome

if grep -q "DEBUG = False" ~/Epitome/Epitome/settings.py; then

    sed -i "s/DEBUG = False/DEBUG = True/" ~/Epitome/Epitome/settings.py;
    
    elif grep -q "DEBUG = True" ~/Epitome/Epitome/settings.py; then
    
    sed -i "s/DEBUG = True/DEBUG = False/" ~/Epitome/Epitome/settings.py;

fi
