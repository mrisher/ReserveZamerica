import os
import sys
sys.path.append('/home/mrisher/src/rz')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rz.settings'
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

