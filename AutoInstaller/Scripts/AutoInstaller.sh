#!/bin/bash

echo 'Welcome to the Epitome AutoInstaller'

# Remove previous Epitome installations
rm -rf ~/Epitome/

rm -rf ~/Desktop/epitome/

rm -rf ~/EpitomeVE

# Find out the installed package manager and install required packages
if type apt 2> /dev/null; then
   sudo apt-get install git python3 python3-venv python3-pip
elif type dnf 2> /dev/null; then
   sudo dnf install git python3 python3-virtualenv python3-pip
elif type pacman 2> /dev/null; then
   sudo pacman -S git python python-virtualenv python-pip
else
   echo "Supported package manager not found (apt, dnf, pacman)" >&2
   exit 1
fi

# Clone Epitome repository
cd ~/Desktop

git clone https://github.com/TheDemocracyFoundation/epitome.git

cd ~/Desktop/epitome

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

cd ~/Desktop/epitome/

cp -rf * ~/Epitome

rm -rf ~/Desktop/epitome/

cd ~/Epitome

python3 manage.py makemigrations Demoscopesis

python3 manage.py makemigrations Agora

python3 manage.py makemigrations Propylaea

python3 manage.py migrate 

exit
