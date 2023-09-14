#!/bin/usr/python3
import os
import sys

sys.path.append('/data/data/com.termux/files/home/project/anoda/')

from flask_login import LoginManager
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
#flask_mail import Moment__init__
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
db = SQLAlchemy()

#def create_app(config_name):
app = Flask(__name__)
app.config.from_object(config['default'])
config['default'].init_app(app)
migrate = Migrate(app, db)
db.init_app(app)
login_manager = LoginManager()
#login_manager.login_view = 'admin.login'
login_manager.init_app(app)
bootstrap.init_app(app)
#mail.init_app(app)

#attach routes and custom error pages here
from app.products.products import product_bp
from app.customers.customers import customer_bp
from app.auth.auth import auth_bp
from app.carts.carts import cart_bp
from app.admin.admin import admin_bp
app.register_blueprint(product_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(admin_bp)
#return app

