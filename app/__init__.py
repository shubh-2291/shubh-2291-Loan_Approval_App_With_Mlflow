from flask import Flask

application = Flask(__name__)
application.secret_key = 'loan prediction app by shubham'

from app.models import *