# !/usr/bin/python
import os
import sys
from django.core.wsgi import get_wsgi_application

"""
WSGI config for sigcao project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""


sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'sigcao'))
os.environ["DJANGO_SETTINGS_MODULE"] = "sigcao.settings"

application = get_wsgi_application()
