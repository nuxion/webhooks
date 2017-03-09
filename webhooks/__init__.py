from flask import Flask
from webhooks import gitexec
from webhooks import loghelper
import logging

app = Flask(__name__)
#app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('instance/config.py')
loghelper.setup_logging(default_path=app.config['CFG_LOG'])
import webhooks.webhooks

