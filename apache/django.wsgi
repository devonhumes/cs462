import os
import sys

path = '/usr/local/django'
if path not in sys.path:
    sys.path.insert(0, '/usr/local/django')

os.environ['DJANGO_SETTINGS_MODULE'] = 'cs462.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
