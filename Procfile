release: python3 configure_env.py && python3 manage.py makemigrations Demoscopesis && python3 manage.py makemigrations Agora && python3 manage.py makemigrations Propylaea && python3 manage.py migrate
web: gunicorn Epitome.wsgi --log-file -
