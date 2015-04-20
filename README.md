# Group 27 CS 309 - Group Event Planner
An event planner for group events such as dinners and hiking trips.

### Setup Directions

(1) Change you permissions on a directory (preferably in /var/www) so that you have read and write permissions on it.

(2) Clone this repository into that directory.

(3) edit /etc/nginx/sites-available/default as described below:

    There is a section labelled "location".  Replace the section with the text below.

	location ~ {

		proxy_set_header Host $host;

		proxy_set_header X-Real-IP $remote_addr;

		proxy_pass http://localhost:8000;

		# First attempt to serve request as file, then

		# as directory, then fall back to displaying a 404.

		# try_files $uri $uri/ =404;

		# Uncomment to enable naxsi on this location

		# include /etc/nginx/naxsi.rules

	}

(3b) Type "sudo nginx -s reload" to reload the configuration for nginx.

(4) In the folder you clone the git repository and there is the file "manage.py", run "gunicorn planner.wsgi"

### Directions to setup networking so that you can view your webpage

(1)  Edit /etc/network/interfaces as root.  There should be two lines: "auto eth0" and "iface eth0 inet dhcp".  Copy those two lines and replace eth0 with eth1.  

(2)  Shutdown the virtual machine.

(3)  Go to the settings for the virtual machine in VirtualBox.  Click on Network, then Adapter 2.  In the drop-down, select "Host-only Adapater".  Hit OK to exit the menus.

(4)  Power on the virtual machine.

(5)  Restart the server by running gunicorn planner.wsgi in the directory with manage.py

(6) Run "ifconfig"  There will be a section labelled "eth1".  On the second line in that section (starting "inet addr:") There wil be an IP address.  On your host machine, enter this ip address in the address bar of your web browser and press enter.  A default Django website should appear.

### Setup so that you can use SSH, SCP, and SFTP to connect

(1) Install the SSH server by running "sudo apt-get install openssh-server"

(2) Follow the directions in the section above to setup networking so that you can access your VM from your host machine.

(3a) If using a Mac, in the Mac's terminal, enter ssh -l <username> <ip_address> where <username> is your username on the virtual machine and <ip_address> is the IP address of the virtual machine.

(3b) If using FileZilla, in the host box, enter "sftp://ip_address" (replace IP address with the IP address). Fill in your username and password for the VM and hit Quickconnect.

### Using Tmux

(1) To install, type "sudo apt-get install tmux"

Your current tmux window is outlined in green.

To enter tmux commands, you first have to press Control+B, then you can type the commands to add windows, resize windows, and more.  Type exit to close out of a tmux window.  The current Below are the most useful tmux commands.

" = split horizontally

% = split vertically

Arrow keys = move between tmux windows

ALT+Arrow Keys or CTRL+Arrow keys = resize current tmux window

[ = scroll, type "q" to exit and be able to type into the terminal again.

### Requirements to Run the PLANtastic server
You will need to run these commands in order to migrate the database: (NOTE: You only need to do these once per install)
1. sudo apt-get install python-mysql
2. sudo pip install libnet-smtp-ssl-perl (required for email functionality)
3. sudo pip install django-localflavor (required for weather tool)
