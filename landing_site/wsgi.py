"""
WSGI config for landing_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "landing_site.settings")

from whitenoise.django import DjangoWhiteNoise  # noqa

application = DjangoWhiteNoise(get_wsgi_application())
