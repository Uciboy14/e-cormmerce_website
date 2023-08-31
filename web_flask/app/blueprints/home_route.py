import os
import sys

working_path = os.getcwd()
parent_dir = os.path.dirname(working_path)
sub_parent = os.path.dirname(parent_dir)
sys.path.append("/data/data/com.termux/files/home/e-cormmerce_website/")

from flask import Blueprint, render_template
from models import storage

home_bp = Blueprint("home", __name__)

@home_bp.route('/', strict_slashes=False)
@home_bp.route('/index', strict_slashes=False)
def index():
	return render_template('index.html')

@home_bp.route('/contact', strict_slashes=False)
def contact_us():
	return render_template('contact.html')

@home_bp.route('/shop', strict_slashes=False)
def shop_fun():
	return render_template('shop.html')
