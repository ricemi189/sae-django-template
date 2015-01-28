# coding: utf-8
#
"""
Demo index for sae-django-template.

"""

from django.http import HttpResponse


def home(request):
    msg = "It works!"
    return HttpResponse(msg)
