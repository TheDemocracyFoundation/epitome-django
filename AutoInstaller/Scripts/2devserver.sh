#!/bin/bash

source ~/EpitomeVE/bin/activate

cd ~/Epitome

symbols=({a..z} {A..Z} {0..9} '_' '-' '#' '$' '%' '^' '&' '*' '(' ')' '!' '@') length=50 EPITOME_SECRET_KEY=; for (( i = 0; i < length; i++ )); do EPITOME_SECRET_KEY+=${symbols[RANDOM%${#symbols[@]}]}; done; export EPITOME_SECRET_KEY

python3 manage.py runserver
