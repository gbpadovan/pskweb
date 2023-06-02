import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application



if settings.USE_VERCEL:
    # if hosting is Vercel:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings")
    application = get_wsgi_application()
    app = application

else:
    # use local host
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "psk.settings")
    application = get_wsgi_application()
