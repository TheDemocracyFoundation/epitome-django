#!/bin/bash

read -r -p "Are you sure you want to completely remove Epitome from your system? [y/n]  " response
 response=${response,,} # tolower
 echo    # move to a new line
 if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then
    rm -rf ~/Epitome/

    rm -rf ~/tempepitome

    rm -rf ~/EpitomeVE
 fi
