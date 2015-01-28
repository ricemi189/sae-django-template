#!/usr/bin/env python
import os
import sys

DEBUG = not ('SERVER_SOFTWARE' in os.environ)
root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)

if DEBUG:
    os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.settings.local'
    sys.path.insert(0, os.path.join(root, 'site-packages'))
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = '{{ project_name }}.' \
        'settings.production'

sys.path.insert(0, os.path.join(root, 'site-packages.zip'))

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
