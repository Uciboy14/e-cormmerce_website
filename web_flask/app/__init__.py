import sys

#sys.path.append("/home/uc-code_tech/my-projects/e-cormmerce_website/web_flask/")

from flask import Flask
from app.home_route import home_bp
from app.category_route import category_bp
from app.cart_route import cart_bp
from app.checkout_route import checkout_bp
from app.product_route import product_bp

def create_app():
	app = Flask(__name__)

	#configuration
	app.config.from_pyfile('../config.py')

	#Register blueprints
	app.register_blueprint(home_bp)
	app.register_blueprint(category_bp)
	app.register_blueprint(cart_bp)
	app.register_blueprint(checkout_bp)
	app.register_blueprint(product_bp)

	#from app.api import api_bp
	#app.register_blueprint(api_bp, url_prefix='/api') 

	return app