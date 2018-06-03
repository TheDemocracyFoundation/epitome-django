#!/bin/bash

read -r -p "Are you sure you want to update Epitome? This will not replace your database contents but it will replace config files such as your settings.py [y/n]  " response
 response=${response,,} # tolower
 echo    # move to a new line
 if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then
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
fi
