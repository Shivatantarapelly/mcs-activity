"""
ASGI config for Familyexpensetracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
django.setup()


from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Familyexpensetracker.settings')

application = get_asgi_application()
