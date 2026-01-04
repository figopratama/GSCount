"""
WSGI config for gscount project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
>>>>>>> origin/main
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gscount.settings')

application = get_wsgi_application()
