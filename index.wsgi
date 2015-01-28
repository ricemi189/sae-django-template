#coding:utf-8

import sae
import os
import django.core.handlers.wsgi
import sys

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)

DEBUG = not ('SERVER_SOFTWARE' in os.environ)


if DEBUG:
    os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.settings.local'
    sys.path.insert(0, os.path.join(root, 'site-packages'))
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.settings.production'
sys.path.insert(0, os.path.join(root, 'site-packages.zip'))

application=sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())
