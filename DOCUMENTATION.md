# Epitome documentation

## Installation

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/TheDemocracyFoundation/epitome)

If you choose to install Epitome on Heroku, please click the button above, the fields of the required variables should be already populated (such as the the required config variable "EPITOME_SECRET_KEY", which should contain a 50-character string including numbers and symbols. You can use [an online tool to help you with the key generation](https://www.miniwebtool.com/django-secret-key-generator/)).

In order to create an admin account you must go to More > Run console, run the command

`python3 manage.py createsuperuser`

and fill in the admin account information.

To visit the administration page, go to https://name-of-your-app.herokuapp.com/admin/ (replace the app name in the address with yours).

### Autoinstaller

For most Linux distributions, you can take a look at the [Autoinstaller script](AutoInstaller/) that downloads and installs Epitome to your system with a few clicks.

### Manual installation in Linux operating systems

<p align="justify">In order to install Epitome, python 3 must be installed in order to create a virtual environment. After that, django must be installed via pip. Create a new project using django’s “startproject” command, and in that new project, import the Epitome files. Epitome will be finally set up using the settings.py script and will run using the embedded server.</p>

Please note that this guide assumes that the `python` alias in your operating system's bash is pointing to python version 2. If you run the command `python --version` and you get python 3 (such as in Gentoo and Arch based linux distributions), you will have to run the commands that follow as `python` instead of `python3`.

In an Ubuntu based operating system:

1) It is recommended that you first update your operating system by typing:

`sudo apt update`

`sudo apt full-upgrade`

2) [Download the repository from GitHub](https://help.github.com/articles/cloning-a-repository/) somewhere in your desktop (so it won't interfere with the folder we will create in your home directory).

3) Install required dependencies:

`sudo apt install python3`

and

`sudo apt install python3-venv`

4) Install pip by typing:

`sudo apt install python3-pip`

5) The version already installed may be outdated. Update by typing:

`sudo pip3 install --upgrade pip setuptools`

6) Go to the home directory and create a new directory for the virtual environment:

`cd ~`

and

`mkdir EpitomeVE`

7) Specify the system python3 installation:

`python3 -m venv EpitomeVE/`

8) Activate the virtual environment:

`source ~/EpitomeVE/bin/activate`

upgrade pip3 again in case it requires it

`pip3 install --upgrade pip`

Install django and whitenoise

`pip3 install django whitenoise`

9) Create a new folder Epitome in your home folder:

`mkdir ~/Epitome/`

10) Move all the contents the folder which you downloaded from our repository to the newly created folder

11) Set the secret key file as an environmental variable in your system. It should be 50 random characters and it should be named "EPITOME_SECRET_KEY".

12) From the terminal, change the directory into the newly created folder and make the database migrations by typing:

`cd ~/Epitome`

and

`python3 manage.py makemigrations Demoscopesis`

`python3 manage.py makemigrations Agora`

`python3 manage.py makemigrations Propylaea`

`python3 manage.py migrate`

`python manage.py collectstatic`


13) To start django server move to the folder Epitome and start the server by typing:

`python3 manage.py runserver`

14) To create an admin account, open a new terminal, re-activate the virtual environment with:

`source ~/EpitomeVE/bin/activate`

`cd ~/Epitome`

and follow the instructions after typing:

`python3 manage.py createsuperuser`

15) Open your web browser to access the admin panel in this address:

<http://localhost:8000/admin/>

16) To access Epitome enter the following address:

<http://localhost:8000/user/login>

*Usernames are case-sensitive.

You should now have a working instance of Epitome.

-----------------------------------

### Operation

1) Enter the Admin page by inserting your information.

<img src="https://i.imgur.com/bg02gpF.png">

2) This will bring you to the admin landing page.

<img src="https://i.imgur.com/L0RD0x0.png">

3) Click "Groups" to go into the groups section, and press "Add group" on the top right corner.

<img src="https://i.imgur.com/zXXIa9X.png">

4) Create a new admin group, give all permissions and press save.

<img src="https://i.imgur.com/glcHosT.png">

5) You should now have an admin group.

<img src="https://i.imgur.com/IAcce5o.png">

6) You can register users manually through the admin page, simply click on "Add" next to the "Users" in the main admin page, add the info and press save.

<img src="https://i.imgur.com/EBRqSBB.png">

7) Before creating proposals, you need to create a category first, from the main adming page, click on "Add" next to the "Proposal cats", add the name of the category and press save.

<img src="https://i.imgur.com/evFFYMS.png">

8) To create a new proposal, click on "Add" next to the "Proposals", add the information for the proposal and click save.

<img src="https://i.imgur.com/6iBnUp9.png">

<img src="https://i.imgur.com/6lGLHzu.png">

9) A user can also register by clicking "Create an account" on the login page (<http://localhost:8000/user/login>)

<img src="https://i.imgur.com/SjNJd1H.png">

<img src="https://i.imgur.com/7Kr2Zbk.png">

10) Login using your account information.

<img src="https://i.imgur.com/Bafghrx.png">

11) This bring you to the main page that should now contain your created proposal.

<img src="https://i.imgur.com/4qskdxn.png">

12) You can vote on the proposal by clicking on it and selecting your choice on the bottom. Once you do, you will be transfered back to the main page and a confirmation message will appear.

<img src="https://i.imgur.com/ILhagwN.png">

<img src="https://i.imgur.com/M0q1xo2.png">

13) If you try to vote again, a message will inform you that you have already voted.

<img src="https://i.imgur.com/FrPeJoW.png">


### Troubleshooting

* Issue: django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named MySQLdb

Solution: install python-mysqldb by writing

 `sudo apt install python-mysqldb`

* Issue: django.db.utils.OperationalError: (2003, "Can't connect to MySQL server on '127.0.0.1' (111)")

Solution: Check if you have correctly configured the fields under the "DATABASES = {" section of the settings.py file.
located inside the "Epitome" folder
 
* Issue: when typing "sudo python manage.py migrate" you get the following
 `'NAME': 'os.path.join(BASE_DIR, 'db.sqlite3')',
                                      ^
SyntaxError: invalid syntax`

Solution: make sure you remove the 'apostrophes' from the "NAME:" field under the "DATABASES = {" section of the settings.py file.

* Issue: You try to run the server again after you closed it and you get the message "Error: That port is already in use."

Solution: kill all the processes associated with port 8000 by typing 

`sudo fuser -k 8000/tcp`

* Issue: Import error, No module named urls

Solution: Change line in file Demoscopesis/views.py

`from django.url import reverse`

to

`from django.core.urlresolvers import reverse`
