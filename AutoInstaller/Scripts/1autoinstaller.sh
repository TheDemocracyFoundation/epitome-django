#!/bin/bash

echo 'Welcome to the Epitome AutoInstaller.'
echo    # move to a new line

read -r -p "Would you like to install Epitome to your system? [y/n]  " response
 response=${response,,} # tolower
 echo    # move to a new line
 if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then

    # Remove previous Epitome installations
    rm -rf ~/Epitome/

    rm -rf ~/tempepitome/

    rm -rf ~/EpitomeVE
echo 'Detecting package manager...'
    # Find out the installed package manager and customize the subsequent scripts
    if type apt 2> /dev/null; then
        echo    # move to a new line
        sudo apt-get install git python3 python3-venv python3-pip
   
        # Clone Epitome repository
        mkdir ~/tempepitome/
        cd ~/tempepitome/

        git clone https://github.com/TheDemocracyFoundation/epitome.git

        cd ~/tempepitome/epitome

        git checkout development

        # Install pip and activate the python virtual environment

        sudo pip install --upgrade pip setuptools

        cd ~

        mkdir EpitomeVE

        python3 -m venv EpitomeVE/

        source ~/EpitomeVE/bin/activate

        pip install --upgrade pip
        
        # Install django and make migrations

        pip install django

        mkdir ~/Epitome/

        cd ~/tempepitome/epitome

        cp -rf * ~/Epitome

        rm -rf ~/tempepitome/

        cd ~/Epitome

        symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 key=; for (( i = 0; i < length; i++ )); do key+=${symbols[RANDOM%${#symbols[@]}]}; done; echo "$key" > ~/Epitome/secret_key.txt

        python3 manage.py makemigrations Demoscopesis

        python3 manage.py makemigrations Agora

        python3 manage.py makemigrations Propylaea

        python3 manage.py migrate
   
    elif type dnf 2> /dev/null; then
        echo    # move to a new line
        sudo dnf install git python3 python3-virtualenv python3-pip
   
        # Clone Epitome repository
        mkdir ~/tempepitome/
        cd ~/tempepitome/

        git clone https://github.com/TheDemocracyFoundation/epitome.git

        cd ~/tempepitome/epitome

        git checkout development

        # Install pip and activate the python virtual environment

        sudo pip install --upgrade pip setuptools

        cd ~

        mkdir EpitomeVE

        python3 -m virtualenv EpitomeVE/

        source ~/EpitomeVE/bin/activate

        pip install --upgrade pip
        

        # Install django and make migrations

        pip install django

        mkdir ~/Epitome/

        cd ~/tempepitome/epitome

        cp -rf * ~/Epitome

        rm -rf ~/tempepitome/

        cd ~/Epitome

        symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 key=; for (( i = 0; i < length; i++ )); do key+=${symbols[RANDOM%${#symbols[@]}]}; done; echo "$key" > ~/Epitome/secret_key.txt

        python3 manage.py makemigrations Demoscopesis

        python3 manage.py makemigrations Agora

        python3 manage.py makemigrations Propylaea

        python3 manage.py migrate
        
    elif type pacman 2> /dev/null; then
        echo    # move to a new line
        sudo pacman -S git python python-virtualenv python-pip
      
        # Clone Epitome repository
        mkdir ~/tempepitome/
        cd ~/tempepitome/

        git clone https://github.com/TheDemocracyFoundation/epitome.git

        cd ~/tempepitome/epitome

        git checkout development

        # Install pip and activate the python virtual environment

        sudo pip install --upgrade pip setuptools

        cd ~

        mkdir EpitomeVE

        python3 -m venv EpitomeVE/

        source ~/EpitomeVE/bin/activate

        pip install --upgrade pip
        
        # Install django and make migrations

        pip install django

        mkdir ~/Epitome/

        cd ~/tempepitome/epitome

        cp -rf * ~/Epitome

        rm -rf ~/tempepitome/

        cd ~/Epitome

        symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 key=; for (( i = 0; i < length; i++ )); do key+=${symbols[RANDOM%${#symbols[@]}]}; done; echo "$key" > ~/Epitome/secret_key.txt

        python3 manage.py makemigrations Demoscopesis

        python3 manage.py makemigrations Agora

        python3 manage.py makemigrations Propylaea

        python3 manage.py migrate
    else
        echo "Supported package manager not found (apt, dnf, pacman)" >&2
        exit 1
    fi
 fi
