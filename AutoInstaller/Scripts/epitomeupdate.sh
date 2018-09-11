#!/bin/bash

read -r -p "Are you sure you want to update Epitome? This will not replace your database contents [y/n]  " response
 response=${response,,} # tolower
 echo    # move to a new line
 if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then
 
    symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 EPITOME_SECRET_KEY=; for (( i = 0; i < length; i++ )); do EPITOME_SECRET_KEY+=${symbols[RANDOM%${#symbols[@]}]}; done; export EPITOME_SECRET_KEY
    
    rm -rf ~/tempepitome
    
    mkdir ~/tempepitome

    cd ~/tempepitome

    git clone https://github.com/TheDemocracyFoundation/epitome.git

    cd ~/tempepitome/epitome

    source ~/EpitomeVE/bin/activate
    
echo 'Updating pip and required packages'
echo    # move to a new line
    if type apt 2> /dev/null; then
        sudo pip3 install --upgrade pip setuptools
        pip3 install --upgrade pip
        pip3 install django whitenoise
    elif type dnf 2> /dev/null; then
        sudo pip install --upgrade pip setuptools
        pip install --upgrade pip
        pip install django whitenoise
    elif type yum 2> /dev/null; then
        sudo pip3 install --upgrade pip setuptools
        pip install --upgrade pip
        pip install django whitenoise
    elif type pacman 2> /dev/null; then
        sudo pip install --upgrade pip setuptools
        pip install --upgrade pip
        pip install django whitenoise
    fi

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
    
    python3 manage.py makemigrations 
    
    python3 manage.py migrate
    
    python3 manage.py collectstatic
    
fi


