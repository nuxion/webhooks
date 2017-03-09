#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
#sys.path.insert(0,"/var/www/html/flaskapp/")
sys.path.append('/var/www/html/webservice')

from webhooks import app as application
