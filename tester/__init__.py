# -*- coding: utf-8 -*-

"""
tester
~~~

Mandrill Tester Web App

:copyright: (c) 2013 by Fictive Kin.
"""

from flask import Flask
import os
from os.path import dirname

# __name__ is 'tester' because this is an __init__.py file
app = Flask(__name__)
FLASK_APP_DIR = dirname(os.path.abspath(__file__))

# Configuration
app.config.from_object('tester.app_settings.Config')

# we load this here so controllers.py can access the app object
from controllers import *

@app.before_request
def make_session_permanent():
    session.permanent = True

# AWS Health Check
@app.route('/health-check')
def health_check():
    return 'OK'
