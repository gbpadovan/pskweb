import os
#from dotenv import load_dotenv

from django.conf import settings
from django.core.wsgi import get_wsgi_application

#load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "psk.settings")
application = get_wsgi_application()
app = application
"""
if settings.IN_PRODUCTION:
    # Vercel hosting:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "psk.settings")
    application = get_wsgi_application()
    app = application

else:
    # use local host
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "psk.settings")
    application = get_wsgi_application()
"""
