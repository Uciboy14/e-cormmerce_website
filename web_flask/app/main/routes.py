import os
import sys

working_path = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(working_path)
project_dir = os.path.dirname(parent_dir)
sys.path.append(parent_dir)

print(project_dir)

from flask import render_template
from main import views_bp
#from app import create_app

@views_bp.route('/', strict_slashes=False)
@views_bp.route('/index', strict_slashes=False)
def index():
	return render_template('index.html')

@views_bp.route('/contact', strict_slashes=False)
def contact():
	return render_template('contact.html')

@views_bp.route('/shop', strict_slashes=False)
def shop_fun():
	return render_template('shop.html')

@views_bp.route('/testimonial', strict_slashes=False)
def testimonial():
	return render_template('testimonial.html')

@views_bp.route('/why', strict_slashes=False)
def why():
	return render_template('why.html')

@views_bp.route('/login', strict_slashes=False)
def login():
	return render_template('login.html')

@views_bp.route('/gifts', strict_slashes=False)
def gifts():
	return render_template('gift.html')

@views_bp.route('/contact', strict_slashes=False)
def contact_us():
	return render_template('contact.html')

@views_bp.route('/categories', defaults={'id': None})
@views_bp.route('/categories/<id>', strict_slashes=False)
def categories(id):
	return render_template('category.html')

@views_bp.route("/products/<id>", strict_slashes=False)
def product(id):
	return render_template('')

@views_bp.route("/checkout")
def checkout():
	return render_template('checkout.html')

@views_bp.route("/")
def cart():
	return render_template('')

