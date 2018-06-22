#!/bin/bash

read -r -p "Are you sure you want to update Epitome? This will not replace your database contents [y/n]  " response
 response=${response,,} # tolower
 echo    # move to a new line
 if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then
    mkdir ~/tempepitome

    cd ~/tempepitome

    git clone https://github.com/TheDemocracyFoundation/epitome.git

    cd ~/tempepitome/epitome

    git checkout development

    source ~/EpitomeVE/bin/activate

    echo    # move to a new line
    read -r -p "Would you like to replace your current settings.py? (this will delete your current configuration) [y/n]  " response
    response=${response,,} # tolower
    echo    # move to a new line
    if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then
        cd ~/tempepitome/epitome

        rsync -Rr * ~/Epitome
        
        rm -rf ~/tempepitome

        cd ~/Epitome

    else
        cd ~/Epitome/Epitome 
    
        mv settings.py settingsold.py
    
        cd ~/tempepitome/epitome

        rsync -Rr * ~/Epitome

        rm -rf ~/tempepitome
        
        cd ~/Epitome/Epitome 
        
        rm settings.py
        
        mv settingsold.py settings.py

        cd ~/Epitome 
    
    fi
    
    python3 manage.py makemigrations Demoscopesis

    python3 manage.py makemigrations Agora

    python3 manage.py makemigrations Propylaea

    python3 manage.py migrate
    
fi


