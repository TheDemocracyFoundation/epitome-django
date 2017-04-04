# Epitome Documentation

### Installation

<p align="justify">In order to install Epitome, pip needs to be installed globally. After that, django must be installed. Create a new project using django’s “startproject” command, and in that new project, import the Epitome files. Epitome will be finally set up using the settings.py script and will run using the embedded server.</p>

In an Ubuntu based OS:

1) Update your OS by typing:

`sudo apt update`

`sudo apt full-upgrade`

2) Pip can be downloaded through its official installer get-pip.py by typing:

`wget https://bootstrap.pypa.io/get-pip.py`

3) Install pip by typing:

`sudo python get-pip.py`

or if installed in home folder and a permissions problem arises:

`sudo -H python get-pip.py`

4) The version installed may be outdated. Update by typing:

`sudo pip install upgrade pip`

or if installed in home folder and a permissions problem arises:

`sudo -H pip install upgrade pip`
 
5) Install django by typing:

`sudo pip install Django`

or if installed in home folder and a permissions problem arises:

`sudo -H pip install Django`

6) Create a new project by typing:

`django-admin.py startproject Epitome`

7) Move the contents of Epitome to the newly created folder replacing the existing files (keep your settings.py file separately)

8) Open settings.py and add the secret key that was generated in your local machine, and replace the field for the database which should look like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

9) Make the database migrations by typing:

`sudo python manage.py migrate`

10) To start django server move to the folder Epitome and start the server by typing:

`sudo python manage.py runserver`

11) To create an admin account type and follow the instructions:

`sudo python manage.py createsuperuser`

12) Open your web browser to access the admin panel in this address:

<http://localhost:8000/admin/>

13) To access Epitome enter the following address:

<http://localhost:8000/user/login>

You should now have a working instance of Epitome.

*Usernames are case-sensitive.

-----------------------------------

### Operation

### Troubleshooting

* Issue: django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named MySQLdb

 Solution: install python-mysqldb by writing

 `sudo apt install python-mysqldb`

* Issue: django.db.utils.OperationalError: (2003, "Can't connect to MySQL server on '127.0.0.1' (111)")

 Solution: Check if you have correctly configured the database field in the settings.py file under the "Epitome" folder
