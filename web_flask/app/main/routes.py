import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sub_parent = os.path.dirname(parent_dir)
sys.path.append("/home/uc-code_tech/my-projects/e-cormmerce_website/web_flask/app/")

from flask import render_template
from main import route_bp

@route_bp.route('/', strict_slashes=False)
@route_bp.route('/index', strict_slashes=False)
def index():
	return render_template('index.html')

@route_bp.route('/contact', strict_slashes=False)
def contact():
	return render_template('contact.html')

@route_bp.route('/shop', strict_slashes=False)
def shop_fun():
	return render_template('shop.html')

@route_bp.route('/testimonial', strict_slashes=False)
def testimonial():
	return render_template('testimonial.html')

@route_bp.route('/why', strict_slashes=False)
def why():
	return render_template('why.html')

@route_bp.route('/login', strict_slashes=False)
def login():
	return render_template('login.html')

@route_bp.route('/gifts', strict_slashes=False)
def gifts():
	return render_template('gift.html')

@route_bp.route('/contact', strict_slashes=False)
def contact_us():
	return render_template('contact.html')

@route_bp.route('/categories', defaults={'id': None})
@route_bp.route('/categories/<id>', strict_slashes=False)
def categories(id):
	return render_template('category.html')

@route_bp.route("/products/<id>", strict_slashes=False)
def product(id):
	return render_template('')

@route_bp.route("/checkout")
def checkout():
	return render_template('checkout.html')

@route_bp.route("/")
def cart():
	return render_template('')

