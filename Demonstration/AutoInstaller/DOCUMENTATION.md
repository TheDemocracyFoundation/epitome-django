
### Troubleshooting

* Issue: user is not in sudoers file

Solution: type 

 `su`
 
 On Debian:

`apt-get install sudo nano`

On Fedora:

`dnf install sudo nano`

Type:

EDITOR=nano visudo

And scroll down to the bottom of the document and enter the following:

your_username_here ALL=(ALL)       ALL


* Issue: You try to run the server again after you closed it and you get the message "Error: That port is already in use."

Solution: kill all the processes associated with port 8000 by typing 

`sudo fuser -k 8000/tcp`

* Issue: pip3: command not found

Type: sudo ln -s /usr/local/bin/pip /bin/pip
