release: python3 manage.py makemigrations Demoscopesis && python3 manage.py makemigrations Agora && python3 manage.py makemigrations Propylaea && python3 manage.py migrate
web: run python3 manage.py collectstatic --noinput; gunicorn Epitome.wsgi --log-file -
