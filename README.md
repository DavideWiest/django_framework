### This project is a simple Django Project I use to build and deploy a webapp faster. Adapted for deployment with apache2 and mod_wsgi
Currently, it comes with a ui folder and an api folder. The api folder has some useful things like a url query manager.
I made the structure very template-able to reduce boilerplate code.

##### To start: Switch out all occurances of **PROJECT_NAME** (and PROJECT with the desired project name


Deployment ToDo:
- download project repository from github (git clone github.com/user/repo.git)
- install all modules in requirements.txt (pip3 install -r requirements.txt)
- test run app (python3 manage.py runserver)
- create config file (sudo nano /etc/apache2/sites-available/PROJECT_NAME.conf)
- collectstatic (python3 manage.py collectstatic) (STATIC_ROOT must be defined in settings.py as absolute path)
- restart apache2 (systemctl restart apache2)
- check status, debug if needed (systemctl status apache2)
