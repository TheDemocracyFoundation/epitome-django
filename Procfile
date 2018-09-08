release: python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py collectstatic --noinput
web: gunicorn Epitome.wsgi
