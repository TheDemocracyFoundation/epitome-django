
release: heroku config:set EPITOME_SECRET_KEY=`openssl rand -base64 32` && python3 manage.py makemigrations Demoscopesis && python3 manage.py makemigrations Agora && python3 manage.py makemigrations Propylaea && python3 manage.py migrate
web: gunicorn Epitome.wsgi --log-file -
