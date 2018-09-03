release: python3 manage.py makemigrations Demoscopesis && python3 manage.py makemigrations Agora && python3 manage.py makemigrations Propylaea && python3 manage.py migrate
web: python project/manage.py collectstatic --noinput; gunicorn Epitome.wsgi --log-file -
