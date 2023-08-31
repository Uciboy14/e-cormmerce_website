#!/bin/usr/python3
import os
import sys

working_path = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(working_path)
sys.path.append(parent_dir)
print(parent_dir)

from flask import Flask, render_template 
from config import config
#from_bootstrap import Bootstrap
#flask_mail import Moment__init__
from flask_sqlalchemy import SQLAlchemy
import os
import sys

#bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
#db = SQLAlchemy()
        
def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	#bootstrap/init_app(app)
	#mail.init_app(app)

	# attach routes and custom error pages here
	from app.main import route_bp
	app.register_blueprint(route_bp)

	return app

if __name__ == '__main__':
    app = create_app('default')
    @app.teardown_appcontext
    def teardown_appcontext(exception=None):
        storage.close()
