# Epitome Autoinstaller

In order to run the autoinstaller for your system, you should have a non-root user with sudo privileges configured (check troubleshooting below if you don't know how to do this). It is recommended you fully update and upgrade your system before you begin the setup.

In order to install epitome to your system and set up the server, you should run the files by order.

* **1 AutoInstaller**: Currently the package managers supported are apt, dnf and pacman. This file will download required packages, download the epitome repository, create a python 3 virtual environment, install django in the virtual environment, create the django project, copy the files of the repository in the created django project and then make the migrations required for each app.

* **2 (optional) Epitome Run Gunicorn WSGI server**: This is an OPTIONAL file. Run this file only if you want to set up a WSGI Gunicorn server in order host epitome for internet access. If you run this file, it will automatically find your external ip and start a server on it, and therefore you do NOT need to run the dev server (file 2 Epitome Run Dev Server). If you just want to try epitome locally, skip this file. Note, this script will turn django debugging mode off in your settings.py.

* **2 Epitome Run Dev Server**: this file will activate the python 3 virtual environment and then switch to the epitome folder to run the dev server. Note, this script will turn django debugging mode on in your settings.py.

* **3 Epitome Create Admin**: by running this file, you will be prompted to fill in some information to create the superuser (the admin user of epitome).

* **4 Epitome Open Admin**: opening this file, will simply open your browser and direct you to the admin login page. Alternatively, you can visit <http://localhost:8000/admin/>.

* **5 Open Epitome**: opening this file, will simply open your browser and direct you to the epitome login page. Alternatively, you can visit <http://localhost:8000/user/login>.

Other files:
* **Epitome Uninstaller**: This will delete the folders "EpitomeVE" (containing the virtual environment), "tempepitome" and "Epitome" (containing the source code of epitome) from your home directory. This will **not** uninstall the packages that were installed by running the Autoinstaller, you need to remove those manually.

The packages installed in autoinstaller are:

For arch: git, python, python-virtualenv, python-pip

For Debian: git, python3, python3-venv, python3-pip

For Red Hat: git, python3, python3-virtualenv, python3-pip

* **Epitome Updater**: This will download the repository again and replace the files inside your installation. It will not update outdated packages, you need to run a system update for this, and activate your virtual environment to update django. This will not delete your database contents.

Please note that you currently need to create your own secret key and put that in the settings.py file inside the folder Epitome.

# Troubleshooting

#### Issue: You cannot open .desktop files because you are in a SSH session or in a desktop environment which forbits their execution

Solution: you can go into the directory Autoinstaller/Scripts and you can find all the scipts there. In order to run them, you should open a terminal session, change the directory to Autoinstaller/Scripts and then use the commands `chmod a+x filename.sh` and `./filename.sh` to run each individual script. Take a look above for descriptions on what each script does.

#### Issue: `bash: sudo: command not found` or `sudo: No such file or directory` or `user is not in sudoers file`

Solution: type 

`su`
 
On Debian:

`apt-get install sudo nano`

On Fedora:

`dnf install sudo nano`

Type:

`EDITOR=nano visudo`

And scroll down to the bottom of the document and enter the following:

`your_username_here ALL=(ALL)       ALL`

Ctrl + X will quit the editor and you will be asked if you want to save your changes. Press Y for Yes.

------

#### Issue: You try to run the server again after you closed it and you get the message "Error: That port is already in use."

Solution: kill all the processes associated with port 8000 by typing 

`sudo fuser -k 8000/tcp`

------

#### Issue: pip3: command not found

Type: `sudo ln -s /usr/local/bin/pip /bin/pip`
