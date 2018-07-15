from subprocess import call

call("heroku config:set SECRET_KEY=`openssl rand -base64 32`")
call("heroku config:set PYTHONHASHSEED=random")
