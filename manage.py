#!/usr/bin/env python
import os
import sys
from subprocess import call

call("heroku config:set SECRET_KEY=`openssl rand -base64 32`")
call("heroku config:set PYTHONHASHSEED=random")

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')




if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Epitome.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
