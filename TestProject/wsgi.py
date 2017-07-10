"""
WSGI config for TestProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys
sys.path.append('/Library/WebServer/Documents')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestProject.settings")

application = get_wsgi_application()
