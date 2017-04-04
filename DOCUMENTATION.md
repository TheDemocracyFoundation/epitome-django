# Epitome Documentation

### Installation

<p align="justify">In order to install Epitome, pip needs to be installed globally. After that, django must be installed. Create a new project using django’s “startproject” command, and in that new project, import the Epitome files. Epitome will be finally set up using the settings.py script and will run using the embedded server.</p>

In an Ubuntu based operating system:

1) It is recommended that you first update your operating system by typing:

`sudo apt update`

`sudo apt full-upgrade`

2) Pip can be downloaded through its official installer get-pip.py by typing:

`wget https://bootstrap.pypa.io/get-pip.py`

3) Install pip by typing:

`sudo python get-pip.py`

or if installed in home folder and a permissions problem arises:

`sudo -H python get-pip.py`

4) The version already installed may be outdated. Update by typing:

`sudo pip install upgrade pip`

or if installed in home folder and a permissions problem arises:

`sudo -H pip install upgrade pip`
 
5) Install django by typing:

`sudo pip install Django`

or if installed in home folder and a permissions problem arises:

`sudo -H pip install Django`

6) Create a new project by typing:

`django-admin.py startproject Epitome`

**Important: This will create a new folder named "Epitome" in your current directory, go into the newly created folder, find the folder "Epitome" and the file "settings.py" and save it somewhere seperately**

7) Move all the contents of Epitome (the old folder which you downloaded) to the newly created folder replacing all the existing files

8) Open the settings.py that you saved seperately and add the secret key field to the settings.py file in the Epitome folder that was generated in your local machine (and which should now have the settings.py file that you downloaded), it should look somewhat like this:

`SECRET_KEY = 'ibk%9)u6z0c3b$#rm^y1j@nk4@x6es$+dn%f2yx^c87pcf-1)o'
`

9) Replace the information under the "DATABASES = {" section which should look like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

10) From the terminal, change the directory into the newly created folder and make the database migrations by typing:

`cd Epitome`

`sudo python manage.py migrate`

11) To start django server move to the folder Epitome and start the server by typing:

`sudo python manage.py runserver`

12) To create an admin account, open a new terminal, type and follow the instructions:

`sudo python manage.py createsuperuser`

13) Open your web browser to access the admin panel in this address:

<http://localhost:8000/admin/>

14) To access Epitome enter the following address:

<http://localhost:8000/user/login>

*Usernames are case-sensitive.

You should now have a working instance of Epitome.

-----------------------------------

### Operation

1) Enter the Admin page by inserting your information.

![admin-login-page](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/admin-login-page.png)

2) This will bring you to the admin landing page.

![admin-landing-page](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/admin-landing-page.png)

3) Click "Groups" to go into the groups section, and press "Add group" on the top right corner.

![groups-main](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/groups-main.png)

4) Create a new admin group, give all permissions and press save.

![admin-group-creation](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/admin-group-creation.png)

5) You should now have an admin group.

![admin-group-saved](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/admin-group-saved.png)

6) You can register users manually through the admin page, simply click on "Add" next to the "Users" in the main admin page, add the info and press save.

![admin-user-creation](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/admin-user-creation.png)

7) Before creating proposals, you need to create a category first, from the main adming page, click on "Add" next to the "Proposal cats", add the name of the category and press save.

![proposal-cat-creation](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/proposal-cat-creation.png)

8) To create a new proposal, click on "Add" next to the "Proposals", add the information for the proposal and click save.

![proposal-creation](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/proposal-creation.png)

![proposal-creation-done](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/proposal-creation-done.png)

9) A user can also register by clicking "Create an account" on the login page (<http://localhost:8000/user/login>)

![user-register](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/user-register.png)

![register-complete](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/register-complete.png)

10) Login using your account information.

![user-login](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/user-login.png)

11) This bring you to the main page that should now contain your created proposal.

![epitome-landing-page](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/epitome-landing-page.png)

12) You can vote on the proposal by clicking on it and selecting your choice on the bottom. Once you do, you will be transfered back to the main page and a confirmation message will appear.

![proposal](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/proposal.png)

![vote-sucessful](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/vote-sucessful.png)

13) If you try to vote again, a message will inform you that you have already voted.

![already-voted](https://github.com/DemocracyFoundation/Epitome/blob/Development/Demonstration/already-voted.png)


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

Solution: Change line in file Eisegesis/views.py

`from django.url import reverse`

to

`from django.core.urlresolvers import reverse`
