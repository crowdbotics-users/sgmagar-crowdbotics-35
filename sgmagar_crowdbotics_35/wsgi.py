"""
WSGI config for sgmagar_crowdbotics_35 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sgmagar_crowdbotics_35.settings")

application = get_wsgi_application()
