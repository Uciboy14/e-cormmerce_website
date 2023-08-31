#!/bin/usr/python3
import os
import sys

parent_dir = os.getcwd()
working_dir = os.path.dirname(parent_dir)
sys.path.append('/data/data/com.termux/files/home/e-cormmerce_website/web_flask/app/')

from flask import Flask, render_template 
from config import config
#from_bootstrap import Bootstrap
#flask_mail import Moment
from flask_sqlalchemy import SQLAlchemy
import os
import sys

#bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
db = SQLAlchemy()
        

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	#bootstrap/init_app(app)
	#mail.init_app(app)

	# attach routes and custom error pages here
	from main import route_bp
	app.register_blueprint(route_bp)

	return app
