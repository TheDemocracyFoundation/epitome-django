#!/bin/bash
echo 'Epitome'
echo 'Copyright (C) 2015 The Democracy Foundation'
echo 'http://democracy.foundation/'
echo    # move to a new line
echo 'This program is free software: you can redistribute it and/or'
echo 'modify it under the terms of the GNU Affero General Public License'
echo 'as published by the Free Software Foundation, either version 3 of'
echo 'the License, or any later version.'
echo    # move to a new line
echo 'This program is distributed in the hope that it will be useful,'
echo 'but WITHOUT ANY WARRANTY; without even the implied warranty of'
echo 'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the'
echo 'GNU General Public License for more details.'
echo    # move to a new line
echo 'You should have received a copy of the GNU General Public License'
echo 'along with this program. If not, see <https://www.gnu.org/licenses/>.'
echo    # move to a new line
echo    # move to a new line

read -r -p "Would you like to install Epitome to your system? [y/n]  " response
 response=${response,,} # tolower
 echo    # move to a new line
 if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then

echo 'Detecting package manager...'
    # Find out the installed package manager and customize the subsequent scripts
    if type apt 2> /dev/null; then
        echo    # move to a new line
        sudo apt-get install git python3 python3-venv python3-pip rsync
   
        # Clone Epitome repository
        mkdir ~/tempepitome/
        cd ~/tempepitome/

        git clone https://github.com/TheDemocracyFoundation/epitome.git

        cd ~/tempepitome/epitome

        git checkout development

        # Install pip and activate the python virtual environment

        sudo pip3 install --upgrade pip setuptools

        cd ~

        mkdir EpitomeVE

        python3 -m venv EpitomeVE/

        source ~/EpitomeVE/bin/activate

        pip3 install --upgrade pip
        
        # Install django and make migrations

        pip3 install django

        mkdir ~/Epitome/

        cd ~/tempepitome/epitome

        rsync -Rr * ~/Epitome

        rm -rf ~/tempepitome/

        cd ~/Epitome

        symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 key=; for (( i = 0; i < length; i++ )); do key+=${symbols[RANDOM%${#symbols[@]}]}; done; echo "$key" > ~/Epitome/secret_key.txt

        python3 manage.py makemigrations Demoscopesis

        python3 manage.py makemigrations Agora

        python3 manage.py makemigrations Propylaea

        python3 manage.py migrate
   
    elif type dnf 2> /dev/null; then
        echo    # move to a new line
        sudo dnf install git python3 python3-virtualenv python3-pip rsync
   
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

        rsync -Rr * ~/Epitome

        rm -rf ~/tempepitome/

        cd ~/Epitome

        symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 key=; for (( i = 0; i < length; i++ )); do key+=${symbols[RANDOM%${#symbols[@]}]}; done; echo "$key" > ~/Epitome/secret_key.txt

        python3 manage.py makemigrations Demoscopesis

        python3 manage.py makemigrations Agora

        python3 manage.py makemigrations Propylaea

        python3 manage.py migrate
        
          
    elif type yum 2> /dev/null; then
        echo    # move to a new line
        sudo yum install -y epel-release git python36 python34-setuptools python34-pip nss curl libcurl rsync

        sudo pip3 install virtualenv

        sudo pip3 install -U pip   

        # Clone Epitome repository
        mkdir ~/tempepitome/
        cd ~/tempepitome/

        git clone https://github.com/TheDemocracyFoundation/epitome.git

        cd ~/tempepitome/epitome

        git checkout development

        # Install pip and activate the python virtual environment

        sudo pip3 install --upgrade pip setuptools

        cd ~

        mkdir EpitomeVE

        python3 -m virtualenv EpitomeVE/

        source ~/EpitomeVE/bin/activate

        pip install --upgrade pip

        # Install django and make migrations

        pip install django

        mkdir ~/Epitome/

        cd ~/tempepitome/epitome

        rsync -Rr * ~/Epitome
        
        rm -rf ~/tempepitome/

        cd ~/Epitome

        symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 key=; for (( i = 0; i < length; i++ )); do key+=${symbols[RANDOM%${#symbols[@]}]}; done; echo "$key" > ~/Epitome/secret_key.txt

        python3 manage.py makemigrations Demoscopesis

        python3 manage.py makemigrations Agora

        python3 manage.py makemigrations Propylaea

        python3 manage.py migrate
        
    elif type pacman 2> /dev/null; then
        echo    # move to a new line
        sudo pacman -S git python python-virtualenv python-pip rsync
      
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

        rsync -Rr * ~/Epitome

        rm -rf ~/tempepitome/

        cd ~/Epitome

        symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 key=; for (( i = 0; i < length; i++ )); do key+=${symbols[RANDOM%${#symbols[@]}]}; done; echo "$key" > ~/Epitome/secret_key.txt

        python3 manage.py makemigrations Demoscopesis

        python3 manage.py makemigrations Agora

        python3 manage.py makemigrations Propylaea

        python3 manage.py migrate
    else
        echo "Supported package manager not found (apt, dnf, pacman, yum)" >&2
        exit 1
    fi
 fi
