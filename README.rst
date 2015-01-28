SAE-django-template
=======================

Django template used for SAE environment.

Quick start
------------------

1. Install::

    $ django-admin.py startproject --template=https://github.com/xkong/sae-django-template/archive/master.zip --extension=py,wsgi,yaml,rst project_name
    $ cd project_name
    $ pip install -r requirements.txt

2. Edit `{{ project_name}}/settings/base.py`, change DATABASE settings, EMAIL settings and SAE bucket to yours::

    # POP3 config
    EMAIL_HOST = 'smtp.163.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'user'
    EMAIL_HOST_PASSWORD = 'your_password'
    EMAIL_USE_TLS = False
    SERVER_EMAIL = DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

    .....

    STORAGE_BUCKET_NAME = 'xiaoyu'

    MYSQL_USER = 'root'
    MYSQL_PASS = 'password'
    MYSQL_HOST_M = 'localhost'
    MYSQL_HOST_S = 'localhost'
    
    MYSQL_PORT = '3306'

3. Edit `run_server.bat`, change password to your MySQL password.

4. Make a directory in `storage` named of your STORAGE_BUCKET_NAME. These
   settings are used for sae locally debugging.
