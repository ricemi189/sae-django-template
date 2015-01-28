#!/usr/bin/env python
# coding: utf-8
from .base import *
import os

os.environ['sae.storage.path'] = root('storage')
os.environ['HTTP_HOST'] = 'localhost' 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}
